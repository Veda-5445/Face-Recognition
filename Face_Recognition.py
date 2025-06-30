#*** Computer Vision takes any form of pixel data
import cv2

#** Haarcascade is a pretrained face recognition detector
#** Haarcascade algorithm contains XML file contain face characterisitics and features means edge features and line features and eyes, nose properties 
#** cv2.data.haarcascades is an path to xml file
#** cv2.CascadeClassifier loads the algorithm and its features stored in openCV  
haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
if haar_cascade.empty():
    print("haarcascade doesnot load properly")
    exit()

#** cv2 caaptures the video as CamID is 0 - builtin camera and 1 - USB camera , 2 - external Camera
video_capture = cv2.VideoCapture(0)
if not video_capture.isOpened():
    print("error: couldnot load webcam")
    exit()
    
while True:
    #** ret - boolean(TRUE,FALSE) 
    #** frame - (height,width,color) - (255,566,9)
    ret,frame = video_capture.read()
    if not ret:
        print("error: couldnot read frame")
        break

    #** convert frame into gray image
    gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #** detectmultiscale - faraway our face it zooms and which scale present in face it adjusts 
    #** scale_factor- how much image size is reduced at each scale 
    #** min_neighbours - how many rectangles should draw in image
    faces = haar_cascade.detectMultiScale(gray_img,scaleFactor=1.3,minNeighbors=4)

     # Draw rectangles around detected faces
    for (x,y,w,h) in faces:
        
          #** (255,0,0) - color and 6 - thickness                      
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),6)
    
    # Display the video feed
    cv2.imshow("Face Recognition", frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
video_capture.release()
cv2.destroyAllWindows()

    
        
    
    
    
        
    

