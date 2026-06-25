import os
import cv2
from ultralytics import YOLO
from deepface import DeepFace
import matplotlib.pyplot as plt

# 1. Load the lightweight, fast YOLO model for face extraction
# (Using yolov8n/yolov11n as a robust base for bounding boxes)
detector = YOLO("yolov8n.pt")

# 2. Define your database path
DB_PATH = "./school_student_database"


def process_study_desk_frame(image_path):
    # Load the test image (simulating a live webcam frame from the desk)
    frame = cv2.imread(image_path)
    if frame is None:
        print("Error: Image not found!")
        return

    # Keep a copy for drawing the final visual interface
    display_frame = frame.copy()

    # Step 1: Use YOLO to detect human objects/faces
    # classes=0 limits the YOLO detection specifically to humans/persons
    results = detector(frame, classes=0, verbose=False)

    for result in results:
        for box in result.boxes:
            # Extract coordinates of the bounding box
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Step 2: Crop out the detected face area
            # We add a small padding so ArcFace gets enough facial features
            h, w, _ = frame.shape
            pad_x = int((x2 - x1) * 0.1)
            pad_y = int((y2 - y1) * 0.1)

            crop_x1 = max(0, x1 - pad_x)
            crop_y1 = max(0, y1 - pad_y)
            crop_x2 = min(w, x2 + pad_x)
            crop_y2 = min(h, y2 + pad_y)

            face_crop = frame[crop_y1:crop_y2, crop_x1:crop_x2]

            if face_crop.size == 0:
                continue

            try:
                # Step 3: Run ArcFace recognition on the cropped face
                # enforce_detection=False prevents crashes if the crop is tight
                recognition_results = DeepFace.find(
                    img_path=face_crop,
                    db_path=DB_PATH,
                    model_name="ArcFace",
                    enforce_detection=False,
                    silent=True
                )

                # Step 4: Parse results and render UI
                if len(recognition_results) > 0 and not recognition_results[0].empty:
                    # Get the top matching identity path
                    matched_path = recognition_results[0].iloc[0]['identity']

                    # Extract the Student Name from the folder structure
                    student_name = os.path.basename(os.path.dirname(matched_path))
                    color = (0, 255, 0)  # Green for verified
                    label = f"Verified: {student_name}"
                else:
                    color = (0, 0, 255)  # Red for unknown
                    label = "Unknown Student"

            except Exception as e:
                color = (0, 0, 255)
                label = "Unknown Student"

            # Draw the visual UI box around the student
            cv2.rectangle(display_frame, (x1, y1), (x2, y2), color, 3)
            cv2.putText(display_frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    # Step 5: Convert BGR to RGB and display inside Colab notebook
    display_frame_rgb = cv2.cvtColor(display_frame, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(10, 6))
    plt.imshow(display_frame_rgb)
    plt.axis('off')
    plt.show()

# 👉 ACTION REQUIRED: Upload a test image to colab (e.g., 'test_student.jpg')
# and pass it to the function below to see it work!
# process_study_desk_frame("test_student.jpg")
