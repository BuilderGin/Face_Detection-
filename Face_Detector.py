# Supervised Learning
import cv2
from random import randrange

# Load some pre-trained data on face frontals form openCV (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Choose an image to detect faces in
#img = cv2.imread('group.jpeg')
webcam = cv2.VideoCapture(0)

# Iterate forever over frames
while True:
    successful_frame_read, frame = webcam.read()
    
    # Must convert to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Display the image with the faces
    cv2.imshow('Clever Programmer Face Detector', grayscaled_img)

    # Detect face
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    # Draw rectangles around the faces
    for (x, y, w, h) in face_coordinates:
        # cv2.rectangle(image, (first cordinate), (second cordinate), (color in BGR), thikness)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)

    # print(face_coordinates)

    # Display the image with the faces
    cv2.imshow('Clever Programmer Face Detector', frame)
    key = cv2.waitKey(1)

    # if you press q or Q to quit the program
    if key==81 or key==113: #number is found at asciicode
        break

# Release video capture
webcam.release()
print("code compeleted")