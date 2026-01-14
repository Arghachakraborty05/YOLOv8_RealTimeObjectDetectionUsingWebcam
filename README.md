# 🚀YOLOv8_RealTimeObjectDetectionUsingWebcam

This project demonstrates real-time object detection using the YOLOv8s (COCO-pretrained) model through a webcam feed.  
It can detect more than 80 common objects such as Person, Laptop, Mobile, Bottle, Book, Chair, Dog, Cat, and many more.

---

## 🎯 Features

- ✔ Real-time webcam object detection  
- ✔ COCO-pretrained YOLOv8 model  
- ✔ Detects 80+ daily objects  
- ✔ Bounding boxes with confidence percentage  
- ✔ Fast and lightweight  
- ✔ No training required  
- ✔ Beginner-friendly and easy to run  

---

## 🧠 Tech Stack

- Python  
- YOLOv8 (Ultralytics)  
- PyTorch  
- OpenCV  
- NumPy  

---

## 📂 Project Structure

<details> <summary><strong>Click to expand</strong></summary> <br>
YOLO_Webcam/
├── main.py            # Main webcam detection script
├── requirements.txt   # Required libraries
└── README.md          # Project documentation

</details>


# 2️⃣ Install dependencies

pip install -r requirements.txt

# 3️⃣ Run the project
python main.py


# 🖥️ How It Works

The script opens your webcam automatically.

Each frame is passed to the YOLOv8s model.

Detected objects are shown with bounding boxes, labels, and accuracy.

Since the model is trained on the COCO dataset, it can recognize 80+ object classes instantly.

# Example Objects Detected

Person

Laptop

Mobile Phone

Bottle

Book

Chair

Keyboard

Dog

Cat

Car

And many more…

# Requirements

Python 3.8 or above

Webcam

Windows, macOS, or Linux

Internet (only for downloading model on first run)

# Future Improvements

Add FPS counter

Add voice alerts

Add circle-style detection

Add custom YOLO model

Add GUI support
