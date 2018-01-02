#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)


def draw_circle(event, x, y, flags, param):
    """
    左键双击时绘制圆形回调函数
    """
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)


def draw_circle_test():
    """
    显示一副图像，双击时绘制一个圆形
    """
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_circle)

    while True:
        cv2.imshow('image', img)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()


drawing = False  # true if mouse is pressed
mode = True      # if True, draw rectangle. Press 'm' to toggle to curve
ix, iy = -1, -1


def mouse_draw(event, x, y, flags, param):
    """
    显示鼠标轨迹回调，通过m切换绘制类型
    """
    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
        else:
            cv2.circle(img, (x, y), 5, (0, 0, 255), -1)


def draw_change_test():
    """
    绘制鼠标点击轨迹的回调
    """
    global img, mode
    img = np.zeros((512, 512, 3), np.uint8)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', mouse_draw)

    while True:
        cv2.imshow('image', img)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('m'):
            mode = not mode
        elif k == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    # 打印所有的回调事件
    events = [i for i in dir(cv2) if 'EVENT' in i]
    print(events)

    draw_circle_test()
    draw_change_test()


