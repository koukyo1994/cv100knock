import cv2

img = cv2.imread("imori.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

hsv[..., 0] = (hsv[..., 0] + 180) % 360
bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

cv2.imshow("", bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
