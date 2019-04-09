import cv2

img = cv2.imread("imori.jpg")
img[(img >= 0) & (img < 64)] = 32
img[(img >= 64) & (img < 128)] = 96
img[(img >= 128) & (img < 192)] = 160
img[(img >= 192) & (img < 256)] = 224

cv2.imshow("degrade", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
