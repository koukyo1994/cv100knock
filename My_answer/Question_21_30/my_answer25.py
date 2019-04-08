import cv2
import numpy as np

img = cv2.imread("imori.jpg")
a = 1.5
h, w, d = img.shape
new_img = np.zeros((int(a * h), int(a * w), d))
for i in range(new_img.shape[0]):
    for j in range(new_img.shape[1]):
        new_img[i, j, :] = img[int(i / a), int(j / a), :]

new_img = new_img.astype(np.uint8)
cv2.imwrite("answer_25.jpg", new_img)
cv2.imshow("bigger", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
