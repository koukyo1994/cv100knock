import cv2
import numpy as np


def padding(img):
    h, w, d = img.shape
    new_img = np.zeros((h + 2, w + 2, d))
    new_img[1:h + 1, 1:w + 1, :] = img.copy()
    return new_img.astype(np.uint8)


def to_gray(img):
    b = img[..., 0]
    g = img[..., 1]
    r = img[..., 2]
    return (0.2126 * r + 0.7152 * g + 0.0722 * b).astype(np.uint8)


img = cv2.imread("imori.jpg")
pad = padding(img)
gray = to_gray(pad)
out = np.zeros((img.shape[0], img.shape[1]))
for i in range(1, int(img.shape[0] + 1)):
    for j in range(1, int(img.shape[1] + 1)):
        patch = gray[i - 1:i + 2, j - 1:j + 2].copy()
        p_max = np.max(patch)
        p_min = np.min(patch)
        pixel = (p_max - p_min).astype(np.uint8)
        out[i - 1, j - 1] = pixel

out = out.astype(np.uint8)
cv2.imwrite("answer_13.jpg", out)
cv2.imshow("", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
