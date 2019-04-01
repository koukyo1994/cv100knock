import cv2
import numpy as np

img = cv2.imread("imori.jpg")

red = img[:, :, 2]
blue = img[:, :, 0]
green = img[:, :, 1]

y = (0.2168 * red + 0.7152 * green + 0.0722 * blue).astype(np.uint8)
cv2.imwrite("answer_2.jpg", y)
cv2.imshow("gray-scale", y)
cv2.waitKey(0)
cv2.destroyAllWindows()
