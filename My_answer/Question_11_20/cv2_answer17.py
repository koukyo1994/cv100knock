import cv2
import numpy as np

img = cv2.imread("imori.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.array([[0., 1., 0.], [1., -4., 1.], [0., 1., 0.]])
laplacian = cv2.filter2D(img, -1, kernel)
cv2.imshow("laplacian", laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()
