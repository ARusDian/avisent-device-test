# live video from picamera with opencv

import cv2
from picamera2 import Picamera2

picam2 = Picamera2()
picam2.configure(
    picam2.create_video_configuration(main={"format": "XRGB8888", "size": (640, 480)})
)
picam2.start()

cv2.startWindowThread()

while True:
    frame = picam2.capture_array()
    cv2.imshow("picamera2", frame)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows() 
