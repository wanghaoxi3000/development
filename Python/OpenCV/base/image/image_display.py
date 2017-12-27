#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

import cv2
from matplotlib import pyplot as plt


def show_img_with_opencv(imgfile, img_way=cv2.IMREAD_COLOR, window_name='image', size=cv2.WINDOW_NORMAL):
    """
    使用openCV显示图片
    :param imgfile: 图片文件名称
    :param img_way: 显示的图片通道，cv2.IMREAD_COLOR cv2.IMREAD_GRAYSCALE cv2.IMREAD_UNCHANGED
    :param window_name: 窗口名
    :param size: 窗口尺寸，cv2.WINDOW_AUTOSIZE和cv2.WINDOW_NORMAL
    :return: None
    """
    cv2.namedWindow(window_name, size)     # 可选，提前创建一个窗口，
    img = cv2.imread(imgfile, img_way)
    cv2.imshow('image', img)
    cv2.waitKey(0)              # 等待指定的毫秒或按下按键后继续，0表示一直等待
    cv2.destroyAllWindows()     # 关闭窗口，可以通过参数指定关闭的窗口


def write_img(imgfile, name, img_way=cv2.IMREAD_COLOR):
    """
    写入图片
    :param imgfile: 原始图片
    :param name: 新写入图片名称
    :param img_way: 打开图片的通道
    :return: None
    """
    img = cv2.imread(imgfile, img_way)
    cv2.imshow('image', img)
    k = cv2.waitKey(0) & 0xFF  # 64位电脑需要 & 0xFF
    if k == 27:
        cv2.destroyAllWindows()
    elif k == ord('s'):
        cv2.imwrite(name, img)
        cv2.destroyAllWindows()


def show_img_with_matplotlib(imgfile):
    """
    使用Matplotlib来显示图片，openCV 使用BGR 模式，Matplotlib 使用RGB 模式，使用openCV加载彩色图片
    将无法在 Matplotlib中显示。
    :param imgfile: 图片文件名
    :return: None
    """
    img = cv2.imread(imgfile, 0)
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    show_img_with_opencv('bing.jpg', cv2.IMREAD_COLOR)
    time.sleep(2)

    write_img('bing.jpg', 'bing_gray.png', cv2.IMREAD_GRAYSCALE)
    time.sleep(2)

    show_img_with_matplotlib('bing.jpg')
