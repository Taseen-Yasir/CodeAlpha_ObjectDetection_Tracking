# Object Detection and Tracking using YOLOv8

## Overview

This project performs real-time object detection and tracking on video files using YOLOv8 and ByteTrack. The system detects multiple objects such as people, cars, buses, trucks, and motorcycles, assigns unique tracking IDs, and follows them across video frames.

## Features

* Object Detection using YOLOv8
* Multi-Object Tracking using ByteTrack
* Supports video file input
* Tracks people and vehicles with unique IDs
* Displays bounding boxes and labels
* Saves processed output video
* Works on traffic and pedestrian videos

## Technologies Used

* Python
* OpenCV
* Ultralytics YOLOv8
* ByteTrack

## Project Structure

CodeAlpha_ObjectDetection_Tracking/

├── main.py

├── videos/

│   ├── People_Walking.mp4

│   └── Traffic.mp4

├── outputs/

│   └── result.mp4

├── requirements.txt

└── README.md

## Installation

Clone the repository:

git clone <repository-link>

Navigate to the project folder:

cd CodeAlpha_ObjectDetection_Tracking

Install dependencies:

pip install -r requirements.txt

## Running the Project

Run the application:

python main.py

Choose a video:

1 - People Walking

2 - Traffic

The program will process the selected video and display detected and tracked objects.

## Sample Output

Detected Objects:

* Person
* Car
* Bus
* Truck
* Motorcycle

Tracked Output:

* Person ID 1
* Person ID 2
* Car ID 3
* Bus ID 4

The processed video is saved in the outputs folder as:

result.mp4

## How It Works

1. Load a video file.
2. Read video frames using OpenCV.
3. Detect objects using YOLOv8.
4. Track detected objects using ByteTrack.
5. Assign unique IDs to each object.
6. Draw bounding boxes and tracking IDs.
7. Save the processed video.

## Future Improvements

* Live webcam support
* Object counting
* Speed estimation
* Streamlit web interface
* Multiple video upload support

## Author

Taseen Yasir Pritam

## Internship

Developed as part of the CodeAlpha Internship Program.
