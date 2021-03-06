import cv2
import numpy as np

img = cv2.imread("imori.jpg")

for i in range(int(img.shape[0] / 8)):
    for j in range(int(img.shape[1] / 8)):
        for k in range(3):
            patch = img[i * 8:(i + 1) * 8, j * 8:(j + 1) * 8, k].copy()
            p_max = np.max(patch)
            patch = p_max * np.ones((8, 8))
            img[i * 8:(i + 1) * 8, j * 8:(j + 1) * 8, k] = patch

cv2.imwrite("answer_8.jpg", img)
cv2.imshow("max-pooling", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
