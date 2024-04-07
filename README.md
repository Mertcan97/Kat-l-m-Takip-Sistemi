# Computer Vision-Based Attendance Tracking System

The Python application project focuses on employing computer vision for attendance tracking, integrating face recognition technology with user authentication. Its primary goal is to automate attendance-taking for designated classes or events and store the attendance data into a CSV file.

## Features

- User Authentication: The project starts with username and password input. If the username and password are correct, access to the attendance-taking screen is granted.
- Face Recognition: Faces of participants are recognized using face recognition technology from images captured by the camera. Recognized participants are added to the attendance list.
- Attendance Taking: Names of recognized participants along with their entry time and date are saved to a CSV file.
- Interface: A simple user interface is created using the Tkinter library. The interface is designed to guide the user and provide information during the process.

## Requirements

- Python 3.x
- OpenCV
- NumPy
- Face Recognition
- Tkinter
- Pillow

You can install the required libraries using the following command:

```
pip install opencv-python numpy face_recognition pillow
```

## Usage

1. Run the main.py file to start the project.
2. Fill in the username and password fields and click the "Login" button.
3. In the attendance-taking screen, stand in front of the camera and wait for your face to be recognized.
4. Upon successful face recognition, your name will appear on the screen and will be added to the attendance list.
5. Press the ESC key to finish taking attendance.

## Notes

- When editing project files, securely store sensitive information such as usernames and passwords in the main.py file.
- When editing project files, you can update the photos of individuals in the encodeListKnown variable to improve the recognition quality of the camera.
