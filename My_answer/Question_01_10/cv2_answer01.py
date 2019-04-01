import cv2

img = cv2.imread("imori.jpg")
img_split = cv2.split(img)
img2 = cv2.merge([img_split[2], img_split[1], img_split[0]])

cv2.imshow("", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
