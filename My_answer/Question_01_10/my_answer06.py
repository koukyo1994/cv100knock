import cv2

img = cv2.imread("imori.jpg")

for i in range(3):
    under_64 = (img[:, :, i] >= 0) & (img[:, :, i] < 64)
    bet64_128 = (img[:, :, i] >= 64) & (img[:, :, i] < 128)
    bet128_192 = (img[:, :, i] >= 128) & (img[:, :, i] < 192)
    bet192_256 = (img[:, :, i] >= 192) & (img[:, :, i] < 256)
    img[under_64, i] = 32
    img[bet64_128, i] = 96
    img[bet128_192, i] = 160
    img[bet192_256, i] = 224

cv2.imwrite("answer_6.jpg", img)
cv2.imshow("decolor", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
