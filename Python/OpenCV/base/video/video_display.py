#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2


def play_video(filename):
    """
    播放视频文件
    :param filename: 视频文件名
    :return: None
    """
    cap = cv2.VideoCapture(filename)

    while cap.isOpened():
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def write_video(filename):
    """
    垂直翻转输出视频
    :param filename: 视频文件名
    :return: None
    """
    cap = cv2.VideoCapture(filename)

    # 定义输出视频的格式
    fourcc = cv2.VideoWriter_fourcc(*'WMV2')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frame = cv2.flip(frame, 0)
            # write the flipped frame
            out.write(frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    play_video('test.mp4')

    write_video('test.mp4')
