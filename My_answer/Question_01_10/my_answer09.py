import cv2
import numpy as np


def padding(img):
    h, w, d = img.shape
    new_img = np.zeros((h + 2, w + 2, d))
    new_img[1:h + 1, 1:w + 1, :] = img.copy()

    return new_img.astype(np.uint8)


img = cv2.imread("imori_noise.jpg")
pad = padding(img)
kernel = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) * 1 / 16

for i in range(1, int(img.shape[0] + 1)):
    for j in range(1, int(img.shape[1] + 1)):
        for k in range(3):
            patch = pad[i - 1:i + 2, j - 1:j + 2, k].copy()
            pixel = np.sum(kernel * patch).astype(np.uint8)
            img[i - 1, j - 1, k] = pixel

cv2.imwrite("answer_9.jpg", img)
cv2.imshow("", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
