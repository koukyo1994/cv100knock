import cv2
import numpy as np

img = cv2.imread("imori.jpg")
h, w, d = img.shape
m = np.float32([[1., 0., 30], [0., 1., -30]])
dst = cv2.warpAffine(img, m, (h, w))
cv2.imwrite("answer_28.jpg", dst)

cv2.imshow("affine", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
