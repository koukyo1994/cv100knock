import cv2
import numpy as np

img = cv2.imread("imori.jpg")
rad = -np.deg2rad(30)
m = np.float32([[np.cos(rad), -np.sin(rad), 0], [np.sin(rad), np.cos(rad), 0]])
m2 = np.float32([[np.cos(rad), -np.sin(rad), -30],
                 [np.sin(rad), np.cos(rad), 30]])
img1 = cv2.warpAffine(img, m, (img.shape[0], img.shape[1]))
img2 = cv2.warpAffine(img, m2, (img.shape[0], img.shape[1]))
cv2.imwrite("answer_30_1.jpg", img1)
cv2.imwrite("answer_30_2.jpg", img2)

cv2.imshow("rotate", img1)
cv2.imshow("rotate and translate", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
