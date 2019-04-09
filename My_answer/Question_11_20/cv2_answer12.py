import cv2
import numpy as np

img = cv2.imread("imori.jpg")
kernel = np.eye(3, dtype=np.float32) / 3
motion = cv2.filter2D(img, -1, kernel).astype(np.uint8)

cv2.imshow("cv2_motion_filter", motion)
cv2.waitKey(0)
cv2.destroyAllWindows()
