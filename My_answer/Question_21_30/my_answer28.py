import cv2
import numpy as np

img = cv2.imread("imori.jpg")
h, w, dd = img.shape

a = 1.
b = 0.
c = 0.
d = 1.
tx = 30.
ty = -30.

x = np.tile(np.arange(w), (h, 1))
y = np.arange(h).repeat(w).reshape(w, -1)

x_ = a * x + b * y + tx
y_ = c * x + d * y + ty

new_img = np.zeros((h, w, dd), dtype=np.uint8)
new_img[x_, y_] = img[x, y]
cv2.imwrite("answer_28.jpg", new_img)
cv2.imshow("affine", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
