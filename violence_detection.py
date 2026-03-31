import cv2
from ultralytics import YOLO
import torch

model_path = "/Users/manojasher/Desktop/best.pt"
model = YOLO(model_path)

def violence_detection_webcam():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not access the webcam.")
        return

    print("Press 'q' to exit the webcam feed.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        results = model.predict(source=frame, save=False, conf=0.5)
        annotated_frame = results[0].plot()
        cv2.imshow("Violence Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    violence_detection_webcam()