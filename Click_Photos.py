import cv2
import os

# Haar cascade file for face detection
import cv2

haar_file = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"


# Dataset path
datasets = 'datasets'
sub_data = 'Veda'

# Create directory if not exists
path = os.path.join(datasets, sub_data)
os.makedirs(path, exist_ok=True)  

(width, height) = (150, 130)  # Resize dimensions for faces

# Load Haar cascade classifier
face_cascade = cv2.CascadeClassifier(haar_file)
if face_cascade.empty():
    print("error: haarcascade doesnot loaded succcessfully")
    exit()


# Initialize webcam (0 = default camera)
webcam = cv2.VideoCapture(0)


count = 1
while count <= 100:  # Capture 100 face images
    print(f"Capturing image {count}")

    # Read frame from webcam
    ret, im = webcam.read()
    if not ret:
        print("Error: Could not read frame from webcam")
        break

    # Convert to grayscale
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4)

    # Process detected faces
    for (x, y, w, h) in faces:
        # Draw rectangle around the detected face
        cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Crop and resize the face
        face = gray[y:y + h, x:x + w]
        face_resized = cv2.resize(face, (width, height))

        # Save face image to dataset folder
        cv2.imwrite(f"{path}/{count}.png", face_resized)
        count += 1

    # Show the webcam feed with detected faces
    cv2.imshow('Face Capture - OpenCV', im)

    # Exit if 'Esc' key (27) is pressed
    if cv2.waitKey(1) == 27:
        break

# Release resources
webcam.release()
cv2.destroyAllWindows()  
