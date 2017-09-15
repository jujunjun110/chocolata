#!/usr/bin/python
import os
import glob
import cv2
import numpy as np

chromakey_dir = "./chromakey/"
images_dir = "./images/"


def main():
    if not os.path.exists(chromakey_dir):
        os.mkdir(chromakey_dir)

    img_paths = glob.glob(images_dir + "*.png")
    file_names = [path.split('/')[-1] for path in img_paths]
    map(save_chromakey_image, file_names)


def save_chromakey_image(file_name):
    print file_name

    # OpenCV HSV H:0-180, S:0-255, V:0-255
    lower_color = np.array([50, 40, 30])
    upper_color = np.array([80, 255, 255])

    img = cv2.imread(images_dir + file_name)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_color, upper_color)
    inv_mask = cv2.bitwise_not(mask)
    result = cv2.bitwise_and(img, img, mask=inv_mask)

    cv2.imwrite(chromakey_dir + file_name, result)


if __name__ == '__main__':
    main()
