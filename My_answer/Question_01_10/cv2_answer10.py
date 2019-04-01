import cv2

img = cv2.imread("imori_noise.jpg")
median_filtered = cv2.medianBlur(img, 3)

cv2.imshow("", median_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
