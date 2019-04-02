import cv2

img = cv2.imread("imori.jpg")
filtered = cv2.blur(img, (3, 3))

cv2.imshow("", filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
