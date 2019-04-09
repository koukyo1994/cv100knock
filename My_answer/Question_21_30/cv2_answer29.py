import cv2
import numpy as np

img = cv2.imread("imori.jpg")
h, w, _ = img.shape

m1 = np.float32([[1.3, 0, 0], [0, 0.8, 0]])
img1 = cv2.warpAffine(img, m1, (int(1.3 * h), int(0.8 * w)))
m2 = np.float32([[
    1.3,
    0,
    30,
], [0, 0.8, -30]])
img2 = cv2.warpAffine(img, m2, (int(1.3 * h), int(0.8 * w)))
cv2.imwrite("answer_29_1.jpg", img1)
cv2.imwrite("answer_29_2.jpg", img2)

cv2.imshow("resize", img1)
cv2.imshow("scale and translate", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
