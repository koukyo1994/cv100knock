import cv2
import numpy as np

img = cv2.imread("imori.jpg")
a = 1.5
h, w, d = img.shape
new_img = np.zeros((int(a * h), int(a * w), d), dtype=np.uint8)
for i in range(new_img.shape[0] - 1):
    for j in range(new_img.shape[1] - 1):
        x, y = np.floor((i / a, j / a)).astype(np.int)
        i1 = img[x, y, :]
        i2 = img[x + 1, y, :]
        i3 = img[x, y + 1, :]
        i4 = img[x + 1, y + 1, :]
        dx = i / a - x
        dy = j / a - y
        new_img[i, j, :] = ((1 - dx) * (1 - dy) * i1 + dx * (1 - dy) * i2 +
                            (1 - dx) * dy * i3 + dx * dy * i4).astype(np.uint8)

cv2.imwrite("answer_26.jpg", new_img)
cv2.imshow("bi-linear", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
