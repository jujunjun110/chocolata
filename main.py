#!/usr/bin/python
import os
import glob
import cv2
import numpy as np
import functools
import sys

chromakey_dir = "./chromakey/"
images_dir = "./images/"


def main():
    if not os.path.exists(chromakey_dir):
        os.mkdir(chromakey_dir)

    img_paths = glob.glob(images_dir + "*.png")
    file_names = [path.split('/')[-1] for path in img_paths]
    f_name = sys.argv[1] if len(sys.argv) > 1 else 'alpha'
    f = globals()[f_name]
    map(functools.partial(save_chromakey_image, filter_func=f), file_names)

def save_chromakey_image(file_name, filter_func):
    print file_name
    result = filter_func(file_name)
    cv2.imwrite(chromakey_dir + file_name, result)

def alpha(file_name):
    lower_color, upper_color = fetch_color_range()

    img = cv2.imread(images_dir + file_name)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    inv_mask = cv2.bitwise_not(mask)

    b_channel, g_channel, r_channel = cv2.split(img)
    result = cv2.merge((b_channel, g_channel, r_channel, inv_mask))
    return result

def black(file_name):
    lower_color, upper_color = fetch_color_range()

    img = cv2.imread(images_dir + file_name)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_color, upper_color)
    inv_mask = cv2.bitwise_not(mask)
    result = cv2.bitwise_and(img, img, mask=inv_mask)
    return result

def fetch_color_range():
    # OpenCV HSV H:0-180, S:0-255, V:0-255
    lower_color = np.array([50, 100, 70])
    upper_color = np.array([80, 255, 255])
    return lower_color, upper_color

if __name__ == '__main__':
    main()
