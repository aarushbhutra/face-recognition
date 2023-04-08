#Face and Eye Recognition with Movement Detection
This repository contains a Python script that utilizes OpenCV to detect faces and eyes in real-time from a webcam feed. Additionally, it tracks the movement direction of the detected face (up, down, left, or right).

#Dependencies
Python 3.x
OpenCV
#How to Install
Install Python 3.x if you haven't already: https://www.python.org/downloads/
Install OpenCV by running the following command in your terminal or command prompt:

```
pip install opencv-python
```
#How to Use
Clone this repository or download the Python script.
Download the Haar Cascade XML classifiers for face and eye detection
Modify the paths to the XML classifiers in the Python script to match the location where you saved them on your machine:

```
face_cascade = cv2.CascadeClassifier(r'path_to_xml_classifier\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(r'path_to_xml_classifier\haarcascade_eye.xml')
```

#Run the Python script:

```
python face_eye_recognition_movement_detection.py
```

A window will open displaying your webcam feed with real-time face and eye detection. The direction of the face movement will be printed in the terminal or command prompt.
Press the ESC key to exit the program.
#How it Works
The script uses the Haar Cascade classifiers to detect faces and eyes in a grayscale version of the webcam feed. It then draws rectangles around detected faces and eyes in the color feed. The script calculates the center of the detected face and compares it with the previous frame to determine the movement direction (up, down, left, or right) if the movement is significant (greater than 10 pixels).

#Limitations
The script may not work well with faces that are tilted, in profile, or partially obscured. The movement detection is based on a simple comparison between frames and may not be accurate in all scenarios. The script is not optimized for performance and may run slow on low-end hardware.
