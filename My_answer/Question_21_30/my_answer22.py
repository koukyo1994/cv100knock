import cv2
import numpy as np
import matplotlib.pyplot as plt


def control_hist(x, mean_original, std_original, mean_target, std_target):
    return std_target / std_original * (x - mean_original) + mean_target


npy_control = np.vectorize(control_hist)
img = cv2.imread("imori_dark.jpg")
mean_original = img.mean()
std_original = img.std()

controled = npy_control(img, mean_original, std_original, 128,
                        52).astype(np.uint8)
cv2.imwrite("answer_22_1.jpg", controled)
plt.hist(controled.reshape(-1), bins=200)
plt.xlim(0, 255)
plt.ylim(0, 1400)
plt.savefig("answer_22_2.png")

cv2.imshow("controled", controled)
cv2.waitKey(0)
cv2.destroyAllWindows()
