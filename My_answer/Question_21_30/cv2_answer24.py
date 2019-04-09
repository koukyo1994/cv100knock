import cv2
import numpy as np

gamma = 2.2

lookup = np.zeros((256, 1), dtype=np.uint8)
for i in range(256):
    lookup[i][0] = 255 * pow(float(i) / 255, 1.0 / gamma)

img = cv2.imread("imori_gamma.jpg")
img = cv2.LUT(img, lookup)
cv2.imshow("gamma", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
