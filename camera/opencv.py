import cv2

# OpenCV gets image in BGR format
image = cv2.imread("test_image.jpg")

cv2.imshow("opencv", image)

cv2.waitKey(0)

cv2.destroyAllWindows()
