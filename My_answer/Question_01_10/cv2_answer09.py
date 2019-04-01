import cv2

img = cv2.imread("imori_noise.jpg")
gaussian_blured = cv2.GaussianBlur(img, (3, 3), 1.3, 1.3)
cv2.imshow("", gaussian_blured)
cv2.waitKey(0)
cv2.destroyAllWindows()
