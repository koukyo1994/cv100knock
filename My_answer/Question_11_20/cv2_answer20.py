import cv2
import matplotlib.pyplot as plt
plt.style.use("ggplot")

img = cv2.imread("imori_dark.jpg")
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.hist(img.ravel(), 256, [0, 256])
plt.show()
