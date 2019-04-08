import cv2
import numpy as np


def padding(img):
    h, w, d = img.shape
    new_img = np.zeros((h + 2, w + 2, d))
    new_img[1:h + 1, 1:w + 1, :] = img
    return new_img


def to_gray(img):
    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]
    return (0.2126 * r + 0.7152 * g + 0.0722 * b).astype(np.uint8)


img = cv2.imread("imori.jpg")
pad = padding(img)
gray = to_gray(pad)

kernel = np.array([[-2., -1., 0.], [-1., 1., 1.], [0., 1., 2.]])

img2 = np.zeros((img.shape[0], img.shape[0]))

for i in range(1, int(img.shape[0] + 1)):
    for j in range(1, int(img.shape[1] + 1)):
        patch = gray[i - 1:i + 2, j - 1:j + 2]
        pixel = np.sum(kernel * patch)
        img2[i - 1, j - 1] = pixel

img2[img2 < 0] = 0
img2[img2 > 255] = 255

img2 = img2.astype(np.uint8)

cv2.imwrite("answer_18.jpg", img2)

cv2.imshow("Emboss", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
