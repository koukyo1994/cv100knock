import cv2
import numpy as np


def padding(img):
    h, w, d = img.shape
    new_img = np.zeros((h + 3, w + 3, d), dtype=np.uint8)
    new_img[1:h + 1, 1:w + 1, :] = img
    return new_img


img = cv2.imread("imori.jpg")
pad = padding(img)
a = 1.5
h, w, d = img.shape
new_img = np.zeros((int(a * h), int(a * w), d))


def h(t):
    if abs(t) <= 1:
        return (-1 + 2) * abs(t)**3 - (-1 + 3) * abs(t)**2 + 1
    elif 1 < abs(t) <= 2:
        return -1 * abs(t)**3 - 5 * -1 * abs(t)**2 + 8 * -1 * abs(t) - 4 * -1
    elif abs(t) > 2:
        return 0


npy_h = np.vectorize(h)

for i in range(new_img.shape[0]):
    for j in range(new_img.shape[1]):
        x, y = np.floor((i / a, j / a)).astype(int)
        imat = np.array([[
            pad[x - 1, y - 1, :], pad[x, y - 1, :], pad[x + 1, y - 1, :],
            pad[x + 2, y - 1, :]
        ], [
            pad[x - 1, y, :], pad[x, y, :], pad[x + 1, y, :], pad[x + 2, y, :]
        ],
                         [
                             pad[x - 1, y + 1, :], pad[x, y + 1, :],
                             pad[x + 1, y + 1, :], pad[x + 2, y + 1, :]
                         ],
                         [
                             pad[x - 1, y + 2, :], pad[x, y + 2, :],
                             pad[x + 1, y + 2, :], pad[x + 2, y + 2, :]
                         ]])
        dx1, dx2, dx3, dx4 = i / a - (x - 1), i / a - x, (x + 1) - i / a, (
            x + 2) - i / a
        dy1, dy2, dy3, dy4 = j / a - (y - 1), j / a - y, (y + 1) - j / a, (
            y + 2) - j / a
        xmat = np.array([[dx1, dx2, dx3, dx4] for i in range(4)])
        ymat = np.array([[dy1] * 4, [dy2] * 4, [dy3] * 4, [dy4] * 4])
        hmat = npy_h(xmat**2 + ymat**2)

        hsum = hmat.sum()
        for k in range(3):
            isum = (hmat * imat[..., k]).sum()
            pixel = (isum / (hsum + 1e-5)).astype(np.uint8)
            new_img[i, j, k] = pixel

cv2.imwrite("answer_27.jpg", new_img)
cv2.imshow("bi-cubic", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
