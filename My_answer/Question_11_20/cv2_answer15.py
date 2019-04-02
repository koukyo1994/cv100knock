import cv2

img = cv2.imread("imori.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img2 = cv2.Sobel(gray, cv2.CV_32F, 1, 0, ksize=3)
img3 = cv2.Sobel(gray, cv2.CV_32F, 0, 1, ksize=3)

img2 = cv2.convertScaleAbs(img2)
img3 = cv2.convertScaleAbs(img3)

cv2.imshow("horizontal", img2)
cv2.imshow("vertical", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
