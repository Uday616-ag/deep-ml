import numpy as np

def calculate_brightness(img):
    if len(img) == 0:
        return -1

    if not all(len(row) == len(img[0]) for row in img):
        return -1
		
    img = np.array(img)

    if img.size == 0:
        return -1

    row, col = img.shape

    if row != col:
        return -1

    if img.min() < 0 or img.max() > 255:
        return -1

    return np.mean(img)