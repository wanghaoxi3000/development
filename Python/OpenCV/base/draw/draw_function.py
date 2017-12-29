#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import cv2


# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# 绘制长方形，需要指定长方形的左上角和右下角坐标
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

# 绘制圆形，需要指定圆形的中心点和半径
img = cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)

# 绘制椭圆，需要指定椭圆的中心点，长轴和短轴距离，逆时针旋转角，起始和结束角度
img = cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)

# 绘制多边形
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
img = cv2.polylines(img, [pts], True, (0, 255, 255))  # 第三个参数为False时可以指定是否闭合

# 绘制文字
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

# 显示图像
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
