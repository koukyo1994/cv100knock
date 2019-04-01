import cv2

img = cv2.imread("imori.jpg")
img2 = img.copy()

red = img[:, :, 2].copy()
blue = img[:, :, 0].copy()
green = img[:, :, 1].copy()

img2[:, :, 0] = red
img2[:, :, 1] = green
img2[:, :, 2] = blue

cv2.imwrite("answer_1.jpg", img2)
cv2.imshow("image", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
