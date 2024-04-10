import cv2
import mediapipe as mp
import time

# Create a video capture object
cap = cv2.VideoCapture(0)

# Hand tracking module
mpHands = mp.solutions.hands # Hands module, to detect hands, fingers, etc.
hands = mpHands.Hands() # Parameters: static_image_mode, max_num_hands, min_detection_confidence, min_tracking_confidence

mpDraw = mp.solutions.drawing_utils # Drawing utilities

pTime = 0 # Previous time
cTime = 0 # Current time

while True:
    success, img = cap.read() # Read the image from the camera
    # Convert the image to RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Process the image
    results = hands.process(imgRGB)
    # Print the results
    # print(results.multi_hand_landmarks)
    # If there are hands in the image
    if results.multi_hand_landmarks:
        # For each hand
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # Get the height, width and channels of the image
                h, w, c = img.shape
                # Get the x, y coordinates of the landmarks
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                # If the id is 0, draw a circle around the landmark
                if id == 0:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
            # Draw the landmarks
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
       
    # Calculate the frame rate
    cTime = time.time() # Current time
    fps = 1/(cTime - pTime) # Frames per second
    pTime = cTime # Previous time
    # Display the frame rate
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)     
    # Display the image
    cv2.imshow("Image", img) # Display the image
    cv2.waitKey(1) # Wait for 1 millisecond, then continue
    