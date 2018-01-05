#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2

img1 = cv2.imread('image.jpg')
img2 = cv2.imread('opencv.png')

# 在img1上创建一个img2大小的ROI
rows, cols, channels = img2.shape
print(rows, cols, channels)
roi = img1[0:rows, 0:cols]


# 创建Logo的掩码，和掩码的反色图片
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# 将放置Logo的ROI区域的标黑
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# 从Logo图片中只把Logo区域截取出来
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

# # 将logo放到ROI区域中，修改原本的图片
dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
