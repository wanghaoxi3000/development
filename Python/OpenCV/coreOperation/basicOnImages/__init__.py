#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2

img = cv2.imread('image.jpg')

# 获取指定坐标的RGB值
px = img[100, 100]
print(px)

# 获取指定点的blue值
blue = img[100, 100, 0]

# 修改指定点的RGB值
# 注意：Numpy是为数组计算优化的，因此不论时简单的访问每个像素的值还是修改它们都是非常慢和不推荐的
img[100, 100] = [255, 255, 255]

# 推荐通过 array.item() 和 array.itemset() 来分别设置每个像素值
img.item(10, 10, 2)
img.itemset((10, 10, 2), 100)

# 查看图片的行，列和通道值
# 如果图片是灰度图片，返回的元组中只会包含图片的行列值，因此这也是个检测图片是灰度或彩色图片的方法
print(img.shape)

# 选取图片的指定区域，并对指定区域赋值
ball = img[240:270, 330:390]
img[240:270, 100:160] = ball

# 分离和整合图片B G R各通道的颜色
# cv2.split()是一项非常消耗资源的操作，确保只在必要时才使用
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))
# or
# b = img[:,:,0]

# 设置红色像素为0
img[:, :, 2] = 0

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
