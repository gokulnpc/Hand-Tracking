import HandTrackingModule as htm
import cv2
import time

pTime = 0 # Previous time
cTime = 0 # Current time
# Create a video capture object
cap = cv2.VideoCapture(0)
detector = htm.HandDetector()
while True:
        success, img = cap.read() # Read the image from the camera
        detector.findHands(img)
        detector.findPosition(img)
        # Calculate the frame rate
        cTime = time.time() # Current time
        fps = 1/(cTime - pTime) # Frames per second
        pTime = cTime # Previous time
        # Display the frame rate
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)     
        # Display the image
        cv2.imshow("Image", img) # Display the image
        cv2.waitKey(1) # Wait for 1 millisecond, then continue