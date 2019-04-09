import cv2
import matplotlib.pyplot as plt

plt.style.use("ggplot")

img = cv2.imread("imori.jpg")
for i in range(3):
    img[..., i] = cv2.equalizeHist(img[..., i])
plt.hist(img.reshape(-1), 256, [0, 256])
cv2.imshow("histogram equalization", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
