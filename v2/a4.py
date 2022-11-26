import cv2
import numpy as np


def get_hot_pixels():
    dark_img = get_image("./data/dark")
    return np.any(dark_img[:, :] > 0)


def get_stuck_pixels():
    dark_img = get_image("./data/dark")
    light_img = get_image("./data/light")
    return np.any(dark_img[:, :] == light_img[:, :])


def get_dead_pixels():
    light_img = get_image("./data/light")
    return np.any(light_img[:, :] == 0)


def get_image(image_path):
    img_arr = []

    for i in range(10):
        img_read = cv2.imread(image_path + str(i) + ".png", cv2.IMREAD_GRAYSCALE)
        img_arr.append(img_read)

    return np.mean(img_arr, axis=0).astype(np.double)


print(get_hot_pixels())
print(get_stuck_pixels())
print(get_dead_pixels())
