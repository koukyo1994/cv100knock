import cv2

img = cv2.imread("imori.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()