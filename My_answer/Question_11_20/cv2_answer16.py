import cv2
import numpy as np

img = cv2.imread("imori.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
vkernel = np.array([[-1., -1., -1.], [0., 0., 0.], [1., 1., 1.]])
hkernel = np.array([[-1., 0., 1.], [-1., 0., 1.], [-1., 0., 1.]])
vprewitt = cv2.filter2D(img, -1, vkernel)
hprewitt = cv2.filter2D(img, -1, hkernel)

cv2.imshow("vertical", vprewitt)
cv2.imshow("horizontal", hprewitt)
cv2.waitKey(0)
cv2.destroyAllWindows()
