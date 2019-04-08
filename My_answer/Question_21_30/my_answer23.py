import cv2
import numpy as np
import matplotlib.pyplot as plt


def hist(img):
    histogram = np.histogram(img, bins=255)[0]
    cumsum = np.cumsum(histogram)
    return cumsum


def conversion(x, zmax, s):
    zprime = zmax / s * cumsum[int(x)]
    return zprime


npy_conversion = np.vectorize(conversion)
img = cv2.imread("imori_dark.jpg")
out = img.copy()
zmax = 255
s = img.size
sum_h = 0

for i in range(1, 255):
    ind = np.where(img == i)
    sum_h += len(img[ind])
    z_prime = zmax / s * sum_h
    out[ind] = z_prime

cv2.imwrite("answer_23_1.jpg", out)
plt.hist(out.reshape(-1), bins=255)
plt.xlim(0, 255)
plt.ylim(0, 400)
plt.savefig("answer_23_2.png")

cv2.imshow("converted", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
