import cv2
import numpy as np


def get_image(image_path):
    img_arr = []

    for i in range(10):
        img_read = cv2.imread(image_path + str(i) + ".png", cv2.IMREAD_GRAYSCALE)
        img_arr.append(img_read)

    return np.mean(img_arr, axis=0).astype(np.double)


def fix_noise(dark_img, light_img, img):
    img = img - dark_img
    light_img = (light_img - dark_img) / np.mean(light_img)
    img = img / light_img
    return img


res = fix_noise(get_image("./data/dark"), get_image("./data/light"), get_image("./data/default"))
print(res)
cv2.imshow("res", res.astype(np.uint8))

img_dark = get_image("./data/dark")
img_light = get_image("./data/light")

alpha = 3  # Contrast control (1.0-3.0)
beta = 0  # Brightness control (0-100)

adjusted_dark = cv2.convertScaleAbs(img_dark, alpha=alpha, beta=beta)
adjusted_light = cv2.convertScaleAbs(img_light, alpha=alpha, beta=beta)

cv2.imshow('original_dark', img_dark)
cv2.imshow('adjusted_dark', adjusted_dark)

cv2.imshow('original_light', img_light)
cv2.imshow('adjusted_light', adjusted_light)

cv2.waitKey(0)
cv2.destroyAllWindows()
