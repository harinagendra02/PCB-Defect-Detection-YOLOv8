🟩 PCB Defect Detection using YOLOv8

AI-powered Printed Circuit Board (PCB) defect detection system built using a custom-trained YOLOv8-m deep learning model and an interactive Streamlit web application.
The system enables automated inspection, intelligent defect analysis, visual reporting, and downloadable results — designed for industry-grade quality control workflows.

📌 Project Overview

Manual PCB inspection is time-consuming, error-prone, and costly.
This project automates PCB defect detection using computer vision and deep learning, providing:

High-accuracy defect localization

Severity-based defect classification

Professional UI with real-time visualization

Detailed analytical reports for decision-making

The application is optimized with a neon-themed UI for clarity, usability, and modern presentation.

🧠 Defect Classes Detected

The model is trained to detect six critical PCB defects:

Missing Hole

Mouse Bite

Short Circuit

Open Circuit

Spur

Spurious Copper

✨ Key Features
🔍 1. Real-Time YOLOv8 Detection

Custom-trained YOLOv8-m model

Fast and accurate inference

Supports single and multiple image uploads

High-quality bounding box visualization

Automatic severity classification (Low / Medium / High)

📊 2. Intelligent Summary Table

Displays uploaded image list

Shows defect count per image

Shows class-wise defect distribution

One-click “View” button for detailed inspection

🧾 3. Detailed Image Report

For each PCB image, the system provides:

Original input image

Predicted output image with bounding boxes

Dynamic defect table

Per-defect neon UI blocks

Severity badges

Bounding box metadata:

Location

Size

Center coordinates

📈 4. Defect Graph Visualization

Auto-generated bar graph of defect counts

Dark-mode, neon-styled theme

Supports all defect classes

Helps in quick defect trend analysis

🔎 5. Smart Search System

Search images using:

Partial image name

Partial defect name

Example:
Typing mis displays all images containing Missing Hole defects.

📋 6. Image List Panel

Dedicated “List” button

Displays clean list of uploaded images

Clicking an image name opens its full detailed report

Improves navigation for large datasets

📥 7. ZIP Export & Reporting System

Download results in a single ZIP file containing:

Original images

Predicted images

Text defect summary

Auto-generated PDF report

Download options:

Search-filtered results

Entire dataset

⬆️ 8. Floating Scroll-to-Top Button

Smooth navigation for long result pages

Improves usability in multi-image analysis

🏗️ Model & Training Details

Model: YOLOv8-m

Epochs: 80

Batch Size: 16

Optimizer: AdamW

Image Size: 640 × 640

Hardware: NVIDIA RTX 3050 (CUDA enabled)

The model demonstrates strong generalization across all defect classes.

📁 Repository Structure
PCB-Defect-Detection-YOLOv8/
│
├── app.py

├── best.pt

├── requirements.txt

├── README.md

│
├── sample_inputs/
│   ├── sample1.jpg
│   └── sample2.jpg
│

├── outputs/
│   ├── prediction_images/
│   └── defect_graphs/
│


⚙️ Installation & Execution

1️⃣ Install Dependencies

pip install -r requirements.txt

2️⃣ Run the Application

streamlit run app.py

3️⃣ Upload PCB Images


Upload one or multiple PCB images through the UI.

🖼 Sample Results

(Add screenshots in the folders below and link them here)

Original PCB Image

Prediction Output with Bounding Boxes

Defect Count Graph

Auto-Generated PDF Report

🚀 Applications

Automated PCB quality inspection

Smart manufacturing lines

Fault diagnosis systems

Industry 4.0 & smart factory solutions

🔮 Future Enhancements

Video-based PCB inspection

Editable bounding boxes

Cloud deployment (AWS / Streamlit Cloud)

Real-time hardware integration

👨‍💻 Developed By

Hari Nagendra
CSE Student | AI & Computer Vision Enthusiast

⭐ Final Note

This project demonstrates end-to-end AI system development — from model training and backend pipeline to a production-ready interactive application.
