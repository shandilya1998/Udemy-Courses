import cv2

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


"""
    For different OS, different codecs are used
    Windows -- *'DIVX',
    Ubuntu or MacOS -- *'XVID'
"""

writer = cv2.VideoWriter(
    'assets/video_capture_test.mp4',
    cv2.VideoWriter_fourcc(*'XVID'),
    25.0,
    (width, height)
)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Operations here

    writer.write(frame)

    cv2.imshow('gray', gray)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()
