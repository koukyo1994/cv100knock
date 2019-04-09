import cv2

img = cv2.imread("imori.jpg")
h, w, d = img.shape
img = cv2.resize(
    img, (int(h * 1.5), int(w * 1.5)), interpolation=cv2.INTER_CUBIC)
cv2.imshow("cubic", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
