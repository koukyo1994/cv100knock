import cv2
import numpy as np

from function import to_gray


def _calc_var_in_class(binary: np.ndarray, gray: np.ndarray):
    w0 = (binary == 0).mean()
    w1 = (binary == 255).mean()

    mask = (binary == 0)
    masked_img = gray[mask]
    if len(masked_img) > 0:
        M0 = masked_img.mean()
    else:
        M0 = 0
    M1 = gray[~mask].mean()
    return w0 * w1 * (M0 - M1)**2


def threshold_search(gray: np.ndarray):
    candidates = np.arange(0, 255, 1)
    scores = []
    for th in candidates:
        binary = gray.copy()
        binary[binary >= th] = 255
        binary[binary < th] = 0

        score = _calc_var_in_class(binary, gray)
        scores.append(score)
    idx = np.argmax(scores)
    return idx


img = cv2.imread("imori.jpg")
gray = to_gray(img)
threshold = threshold_search(gray)
img2 = gray.copy()
img2[img2 < threshold] = 0
img2[img2 >= threshold] = 255

cv2.imwrite("answer_4.jpg", img2)
cv2.imshow("otsu-binary", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
