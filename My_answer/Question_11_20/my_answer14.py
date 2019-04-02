import cv2
import numpy as np


def padding(img):
    h, w, d = img.shape
    new_img = np.zeros((h + 2, w + 2, d))
    new_img[1:h + 1, 1:w + 1, :] = img.copy()
    return new_img.astype(np.uint8)


def to_gray(img):
    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]
    return (0.2126 * r + 0.7152 * g + 0.0722 * b).astype(np.uint8)


img = cv2.imread("imori.jpg")
pad = padding(img)
gray = to_gray(pad)
vert_kernel = np.array([[0., -1., 0.], [0., 1., 0.], [0., 0., 0.]])
hori_kernel = np.array([[0., 0., 0.], [-1., 1., 0.], [0., 0., 0.]])

img2 = np.zeros((img.shape[0], img.shape[1]))
img3 = np.zeros_like(img2)
for i in range(1, int(img.shape[0] + 1)):
    for j in range(1, int(img.shape[1] + 1)):
        patch = gray[i - 1:i + 2, j - 1:j + 2].copy()
        vert = np.sum(patch * vert_kernel)
        hori = np.sum(patch * hori_kernel)
        img2[i - 1, j - 1] = vert
        img3[i - 1, j - 1] = hori

img2[img2 < 0] = 0
img2[img2 > 255] = 255
img3[img3 < 0] = 0
img3[img3 > 255] = 255

img2 = img2.astype(np.uint8)
img3 = img3.astype(np.uint8)

cv2.imwrite("answer_14_v.jpg", img2)
cv2.imwrite("answer_14_h.jpg", img3)

cv2.imshow("vertical", img2)
cv2.imshow("horizontal", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
