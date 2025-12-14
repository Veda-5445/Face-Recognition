# Face-Recognition
# Face Recognition

## Overview

This is a simple Python-based Face Recognition project that uses a webcam to capture face images and lays the foundation for face detection and recognition using OpenCV. The project is designed for beginners who want to understand how face recognition systems work at a basic level.

The current implementation focuses on capturing face images, which can later be used to train and test face recognition models.

## Project Structure

Face-Recognition/
Click_Photos.py
README.md

Click_Photos.py: Script used to capture images from the webcam and save them for building a face dataset.
README.md: Documentation of the project.

## Features

Capture images using a webcam
Store captured images for dataset creation
Beginner-friendly structure
Easy to extend with training and recognition logic

## Requirements

Python 3.x
OpenCV (cv2)
NumPy

Install required libraries using the following command:

pip install opencv-python numpy

## How to Run the Project

Step 1: Clone the repository

Clone the project from GitHub using:

git clone [https://github.com/Veda-5445/Face-Recognition.git](https://github.com/Veda-5445/Face-Recognition.git)

Step 2: Navigate to the project directory

cd Face-Recognition

Step 3: Run the photo capture script

python Click_Photos.py

This will open your webcam and allow you to capture face images. Follow the instructions shown in the terminal or window.

## Working of the Project

The script accesses the system webcam using OpenCV.
Each frame from the webcam is processed.
Face images are captured and saved to a local directory.
These images can later be used for training a face recognition model.

## Future Enhancements

Add face detection using Haar Cascade or deep learning models
Implement face recognition using LBPH, EigenFace, or FisherFace
Integrate a database to store user details
Build a graphical user interface
Implement real-time face recognition

## Tools and Technologies Used

Python programming language
OpenCV for computer vision tasks
NumPy for numerical operations

## License

This project is open source and can be modified and used for learning and educational purposes.
