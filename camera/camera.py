from picamera2 import Picamera2
import cv2

camera = Picamera2()
cv2.startWindowThread()

camera.configure(camera.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))

camera.start()

camera.wait_for_frames()

# cv2 gets image in BGR format
image = cv2.cvtColor(camera.capture_array(), cv2.COLOR_BGR2RGB)

cv2.imshow("picamera2", image)

cv2.waitKey(0)

cv2.destroyAllWindows()
