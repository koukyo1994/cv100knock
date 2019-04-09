import cv2
import numpy as np

img = cv2.imread("imori.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
vkernel = np.array([[0., -1., 0.], [0., 1., 0.], [0., 0., 0.]])
hkernel = np.array([[0., 0., 0.], [-1., 1., 0.], [0., 0., 0.]])
vdiff = cv2.filter2D(img, -1, vkernel)
hdiff = cv2.filter2D(img, -1, hkernel)

cv2.imshow("vertical", vdiff)
cv2.imshow("horizontal", hdiff)

cv2.waitKey(0)
cv2.destroyAllWindows()
