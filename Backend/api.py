from fastapi import FastAPI, UploadFile, File
from ultralytics import YOLO
import numpy as np
import cv2
import os

app = FastAPI(title="PCB Defect Detection API")

# ---------------- LOAD MODEL ONCE ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "best.pt")

model = YOLO(MODEL_PATH)

# ---------------- HEALTH CHECK ----------------
@app.get("/")
def root():
    return {"status": "PCB Backend is running"}

# ---------------- PREDICTION API ----------------
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Read image bytes
    image_bytes = await file.read()

    # Convert to OpenCV image
    np_img = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    # Safety check
    if img is None:
        return {"boxes": []}

    # Run YOLO inference
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
