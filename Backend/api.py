from fastapi import FastAPI, File, UploadFile
from ultralytics import YOLO
import cv2
import numpy as np

app = FastAPI()   # 🔴 MUST be named `app`

model = YOLO("best.pt")  # model loads once

@app.get("/")
def root():
    return {"status": "PCB Defect API is running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()
    np_img = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    results = model(img)[0]

    boxes = []
    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        boxes.append({
            "x1": x1,
            "y1": y1,
            "x2": x2,
            "y2": y2,
            "confidence": float(box.conf[0]),
            "type": model.names[int(box.cls[0])]
        })

    return {"boxes": boxes}

