# Verlens: Deepfake Detection System 👁️‍🗨️

A full-stack Deepfake Detection System using **Spring Boot** (Java) for frontend/backend integration and a **Flask-based Python API** for image-based deepfake detection using a fine-tuned **EfficientNetB0** CNN model.

---

## 📌 Project Overview

As Artificial Intelligence students, while we strive to push the boundaries of innovation, it is equally our ethical responsibility to ensure AI is used for good. This project aims to detect image-based deepfakes and demonstrate responsible AI in action.

---

## 🧠 Tech Stack

### 🔸 Machine Learning (Python)
- TensorFlow / Keras
- EfficientNetB0 (Transfer Learning)
- Flask REST API

### 🔹 Backend (Java)
- Spring Boot
- REST API
- Multipart File Upload

### 🔸 Frontend
- HTML/CSS/JS (served via Spring Boot)

### 🌐 Infrastructure
- Flask server runs locally (or can be hosted via AWS Lambda or EC2)
- REST communication between Spring Boot and Flask
- Model trained on real vs fake face dataset

---

## 🚀 How It Works

1. **User uploads an image** via a web UI.
2. **Spring Boot backend** receives the file and forwards it to the Flask ML API via REST.
3. **Flask API** processes the image and uses the trained model to predict:
   - Label: **Real** or **Fake**
   - Confidence: % certainty
4. **Result is returned** to Spring Boot and displayed on the frontend.

---

## 👥 Team Members 
- [Chimirala Kowstubha](https://github.com/Kowstubha9)
- [Hitha Choudhary G](https://github.com/hIthachoudhary)
- [Niranjana J](https://github.com/niranjanaj628)


