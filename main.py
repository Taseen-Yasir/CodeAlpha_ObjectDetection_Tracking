from ultralytics import YOLO
import cv2
import os

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

print("1. People Walking")
print("2. Traffic")

choice = input("Choose video (1 or 2): ")

# Project directory
base_dir = os.path.dirname(os.path.abspath(__file__))

# Video selection
if choice == "1":
    video_path = os.path.join(base_dir, "videos", "People_Walking.mp4")
elif choice == "2":
    video_path = os.path.join(base_dir, "videos", "Traffic.mp4")
else:
    print("Invalid choice!")
    exit()

print("\nOpening:")
print(video_path)

# Open video
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("ERROR: Could not open video.")
    exit()

# Create outputs folder if it doesn't exist
output_dir = os.path.join(base_dir, "outputs")
os.makedirs(output_dir, exist_ok=True)

# Output file
output_path = os.path.join(output_dir, "result.mp4")

# Output video settings
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(
    output_path,
    fourcc,
    fps,
    (640, 360)
)

while True:
    success, frame = cap.read()

    if not success:
        print("\nVideo finished.")
        break

    # Resize for faster processing
    frame = cv2.resize(frame, (640, 360))

    # Detection + Tracking
    results = model.track(
        frame,
        persist=True,
        tracker="bytetrack.yaml",
        imgsz=320,
        verbose=False
    )

    annotated_frame = results[0].plot()

    # Save output video
    out.write(annotated_frame)

    # Display
    cv2.imshow("Object Detection & Tracking", annotated_frame)

    key = cv2.waitKey(1)

    if key == ord('q') or key == 27:  # Q or ESC
        print("\nStopped by user.")
        break

# Cleanup
cap.release()
out.release()
cv2.destroyAllWindows()

print("\nOutput saved to:")
print(output_path)