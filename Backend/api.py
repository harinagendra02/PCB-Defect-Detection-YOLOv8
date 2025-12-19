from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from ultralytics import YOLO
import cv2
import tempfile
import os

app = FastAPI()

# Load model ONCE
model = YOLO("models/best.pt")

@app.post("/predict-video/")
async def predict_video(file: UploadFile = File(...)):
    # Save uploaded video
    temp_input = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    temp_input.write(await file.read())
    temp_input.close()

    cap = cv2.VideoCapture(temp_input.name)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    temp_output = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(temp_output.name, fourcc, fps, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model.predict(frame, conf=0.25, verbose=False)
        annotated = results[0].plot()
        out.write(annotated)

    cap.release()
    out.release()

    return FileResponse(
        temp_output.name,
        media_type="video/mp4",
        filename="pcb_defect_output.mp4"
    )
