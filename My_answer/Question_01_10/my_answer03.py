import cv2
import numpy as np

img = cv2.imread("imori.jpg")

red = img[:, :, 2].copy()
blue = img[:, :, 0].copy()
green = img[:, :, 1].copy()

y = (0.2126 * red + 0.7152 * green + 0.0722 * blue).astype(np.uint8)
y[y < 128] = 0
y[y >= 128] = 255

cv2.imwrite("answer_3.jpg", y)
cv2.imshow("binary", y)
cv2.waitKey(0)
cv2.destroyAllWindows()
