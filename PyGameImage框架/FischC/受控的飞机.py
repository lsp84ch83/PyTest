#!/usr/bin/env python
# _*_ coding: utf-8 _*_
'''
@Author  : Soner
@version : 
@Time    : 2017/11/6/0006 22:12
@license : Copyright(C), Your Company 
'''
import pygame
import sys
from pygame.locals import  *

# 初始化pyganme
pygame.init()

size = width, height = 600, 700
speed = [-2, 1]
# 设置背景颜色
bg = (255, 255, 255)

# 创建指定大小的窗口
screen = pygame.display.set_mode(size)
# 设置窗口标题
pygame.display.set_caption("初次见面，请大家多多关照！")

# 加载图片
turtle = pygame.image.load("plane.gif")
# 获得图像的位置矩形
position = turtle.get_rect()

# 设置 左右转向
l_head = turtle
r_head = pygame.transform.flip(turtle, True, False)

# 循环事件
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # 判断是否按下键盘上下左右，并干预飞机走向
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                turtle = l_head
                speed = [-1, 0]
            if event.key == K_RIGHT:
                turtle = r_head
                speed = [1, 0]
            if event.key == K_UP:
                speed = [0, -1]
            if event.key == K_DOWN:
                speed = [0, 1]

    # 移动图像
    position = position.move(speed)
    # 判断是否超过宽度
    if position.left < 0 or position.right > width:
        # 翻转图像 True设置的是水平翻转；False设置的是垂直翻转
        turtle = pygame.transform.flip(turtle, True, False)
        # 反方向移动
        speed[0] = -speed[0]

    # 判断是否超过高度
    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    # 填充背景
    screen.fill(bg)
    # 更新图像
    screen.blit(turtle, position)
    # 更新界面
    pygame.display.flip()
    # 延迟10毫秒
    pygame.time.delay(10)