from ultralytics import YOLO
import cv2

model = YOLO("yolov8s.pt")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]

    for box in results.boxes:
        x1, y1, x2, y2 = box.xyxy[0]

        # Convert to int
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

        conf = float(box.conf[0]) * 100
        cls = int(box.cls[0])
        label = model.names[cls]

        # Draw rectangle
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)

        # Draw text safely
        cv2.putText(
            frame,
            f"{label} {conf:.1f}%",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,255,0),
            2
        )

    cv2.imshow("YOLOv8 COCO Webcam", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
