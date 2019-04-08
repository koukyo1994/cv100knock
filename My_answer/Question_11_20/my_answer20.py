import cv2
import matplotlib.pyplot as plt

img = cv2.imread("imori_dark.jpg")
plt.hist(img.reshape(-1), bins=100)
plt.xlim(0, 250)
plt.ylim(0, 1400)
plt.savefig("answer_20.png")
plt.show()
