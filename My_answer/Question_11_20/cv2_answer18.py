import cv2
import numpy as np

img = cv2.imread("imori.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.array([[-2., -1., 0.], [-1., 1., 1.], [0., 1., 2.]])
emboss = cv2.filter2D(img, -1, kernel)
cv2.imshow("emboss", emboss)
cv2.waitKey(0)
cv2.destroyAllWindows()
