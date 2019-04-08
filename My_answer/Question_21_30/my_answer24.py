import cv2
import numpy as np


def gamma_conversion(x, c, g):
    return (1 / c * x)**(1 / g)


npy_gamma_conversion = np.vectorize(gamma_conversion)
img = cv2.imread("imori_gamma.jpg") / 255
convert = (npy_gamma_conversion(img, 1, 2.2) * 255).astype(np.uint8)

cv2.imwrite("answer_24.jpg", convert)
cv2.imshow("convert", convert)
cv2.waitKey(0)
cv2.destroyAllWindows()
