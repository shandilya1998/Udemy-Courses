import cv2
import time

# This method of reading videos is not meant for display to humans
# It is required to use an appropriate frame rate
cap = cv2.VideoCapture('assets/video_capture_test.mp4')

if cap.isOpened() == False:
    print('File Not Found or wrong codec used')

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        time.sleep(1 / 25.0)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break
cv2.destroyAllWindows()
