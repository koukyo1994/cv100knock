import cv2
import numpy as np
import matplotlib.pyplot as plt

img: np.ndarray = cv2.imread("imori_dark.jpg")
xmin: int = img.min()
xmax: int = img.max()


def normalize(x, xmin, xmax, range_min, range_max):
    if x < xmin:
        return range_min
    elif xmin < x < xmax:
        return (range_max - range_min) / (xmax - xmin) * (x - xmin) + range_min
    else:
        return range_max


npy_normalize = np.vectorize(normalize)
normalized = npy_normalize(img, xmin, xmax, 0, 255).astype(np.uint8)
cv2.imwrite("answer_21_1.jpg", normalized)
plt.hist(normalized.reshape(-1), bins=200)
plt.xlim(0, 255)
plt.ylim(0, 1400)
plt.savefig("answer_21_2.jpg")
cv2.imshow("normalized", normalized)
cv2.waitKey(0)
cv2.destroyAllWindows()
