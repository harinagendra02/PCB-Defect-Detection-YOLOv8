# PCB-Defect-Detection-YOLOv8
AI-powered PCB defect detection using YOLOv8 with Streamlit UI



   🟩 YOLOv8 PCB Defect Detection System

A deep-learning powered application for automated PCB defect detection with a full-featured Streamlit interface, intelligent defect analysis, downloadable reports, and real-time visualization.

📌 Overview

This project uses a custom-trained YOLOv8-m model to detect six major PCB defects:
*Missing Hole

*Mouse Bite

*Short

*Open Circuit

*Spur

*Spurious Copper

The system provides high-accuracy defect detection, generates a detailed analytical report, and offers a smooth UI optimized with a neon theme for better readability and user experience.

✨ Key Features
🔍 1. YOLOv8 Real-Time Defect Detection

Fast and accurate inference

Supports multiple image uploads

High-quality bounding box visualization

Severity classification (Low / Medium / High)

📊 2. Intelligent Summary Table

Shows defect counts per image

Shows per-class defect distribution

Clickable “View” button displays full detailed report

🧾 3. Detailed Image Report

Each image report contains:

Original Image

Prediction Image

Dynamic defect table

Per-defect neon UI blocks

Severity badges

Bounding box details (Location, Size, Center)

📈 4. Defect Graphs

Auto-generated bar graph for defect count

Clean dark-mode theme

Supports all classes in dataset

🔎 5. Smart Search System

Search by:

Partial filename

Partial defect name

Example:
Typing "mis" shows all missing hole images.

📥 6. ZIP Export System

Exports:

Original images

Predicted images

Text defect summary

Auto-generated PDF report

Available for:

Search results only

Entire dataset

📋 7. Image List Feature

“List” button shows a clean list of uploaded images

Clicking an image instantly opens its detailed report

⬆️ 8. Floating Scroll-to-Top Button

Easy navigation for long result pages.

🏗 Model Information

Model: YOLOv8-m

Epochs: 80

Batch size: 16

Optimizer: AdamW

Image size: 640

Device used: NVIDIA RTX 3050

📁 Repository Structure
PCB-Defect-Inspector/
│
├── app.py
├── best.pt
├── requirements.txt
├── README.md
│
├── sample_inputs/
│    ├── sample1.jpg
│    └── sample2.jpg
│
└── docs/
     └── PCB_Report.pdf

⚙️ How to Run the Application
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Run Streamlit App
streamlit run app.py

3️⃣ Upload Images

You can upload one or multiple PCB images.

🖼 Sample Output

(Add screenshots here)

📸 Original Image  
📸 Prediction Image  
📈 Defect Graph  
📝 PDF Report  

🚀 Applications

Industry-level PCB quality inspection

Automated manufacturing line monitoring

Fault diagnosis systems

Smart factories & Industry 4.0 solutions

🔮 Future Improvements

Support for video PCB inspection

Add bounding box editing tool

Cloud deployment (AWS / Streamlit Cloud)

Real-time microcontroller integration

👨‍💻 Developed By

Hari Nagendra
CSE Student | AI Enthusias
