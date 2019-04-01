import numpy as np


def to_gray(img: np.ndarray):
    red = img[:, :, 2].copy()
    blue = img[:, :, 0].copy()
    green = img[:, :, 1].copy()

    y = (0.2126 * red + 0.7152 * green + 0.0722 * blue).astype(np.uint8)
    return y
