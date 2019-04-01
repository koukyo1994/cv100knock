import cv2
import numpy as np


def rgb2hsv(img_original):
    img = img_original.copy().astype(np.float32) / 255.
    arr_max = np.max(img, axis=2).copy()
    arr_min = np.min(img, axis=2).copy()
    argmin = np.argmin(img, axis=2)

    h_arr = np.zeros_like(arr_max)
    h_arr[np.where(arr_max == arr_min)] = 0

    idx_b = np.where(argmin == 0)
    idx_r = np.where(argmin == 2)
    idx_g = np.where(argmin == 1)
    r = img[..., 2].copy()
    g = img[..., 1].copy()
    b = img[..., 0].copy()
    h_arr[idx_b] = 60 * (g[idx_b] - r[idx_b]) / (
        arr_max[idx_b] - arr_min[idx_b]) + 60
    h_arr[idx_r] = 60 * (b[idx_r] - g[idx_r]) / (
        arr_max[idx_r] - arr_min[idx_r]) + 180
    h_arr[idx_g] = 60 * (r[idx_g] - b[idx_g]) / (
        arr_max[idx_g] - arr_min[idx_g]) + 300

    v = arr_max
    s = arr_max - arr_min
    hsv = np.zeros_like(img)

    hsv[..., 0] = h_arr
    hsv[..., 1] = s
    hsv[..., 2] = v
    return hsv


def hsv2rgb(img):
    c = img[..., 1].copy()
    h_ = img[..., 0].copy() / 60
    x = c * (1 - np.abs(h_ % 2 - 1))
    v = img[..., 2].copy()
    z = np.zeros_like(c)
    rgb = np.zeros_like(img)

    vals = [[z, x, c], [z, c, x], [x, c, z], [c, x, z], [c, z, x], [x, z, c]]
    for i in range(6):
        ind = np.where((i <= h_) & (h_ < i + 1))
        rgb[..., 0][ind] = vals[i][0][ind] + (v - c)[ind]
        rgb[..., 1][ind] = vals[i][1][ind] + (v - c)[ind]
        rgb[..., 2][ind] = vals[i][2][ind] + (v - c)[ind]
    rgb = (rgb * 255).astype(np.uint8)
    return rgb


img = cv2.imread("imori.jpg")
hsv = rgb2hsv(img)

hsv[..., 0] = (hsv[..., 0] + 180) % 360
rgb = hsv2rgb(hsv)

cv2.imwrite("answer_5.jpg", rgb)
cv2.imshow("rgb", rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
