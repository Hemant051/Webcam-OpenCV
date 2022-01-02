# Webcam Frames Capturing
import cv2
import numpy as np

#seting the frame ratio
frameWidth = 640
frameHeight = 480

#Command to capture video from external webcam
vid = cv2.VideoCapture(1)
# to set the width of the frame
vid.set(3,640)
# to set the height of the frame
vid.set(4,480)
# to set the brightness of the frame
vid.set(10,150)

# Applying the loop to capture the read the frames of video
while True:
    # check is the variable for checking the boolean values and frame is another variable for storing the readed frames from the video
    check,frame = vid.read()

    #showing the frames captured
    cv2.imshow("webcam video", frame)
    # conditional statement for stoping the frames display
    if cv2.waitKey(1) & 0XFF == ord("q"):
        break
# Terminating commands
vid.release()
cv2.destroyAllWindows()