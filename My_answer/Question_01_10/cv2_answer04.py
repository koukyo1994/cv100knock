import cv2

img = cv2.imread("imori.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, img_threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
cv2.imshow("", img_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
