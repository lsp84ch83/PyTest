#!/usr/bin/env python
# _*_ coding: utf-8 _*_
'''
@Author  : Soner
@version : 
@Time    : 2017/11/6/0006 21:46
@license : Copyright(C), Your Company 
'''
import pygame
import sys

# 初始化pyganme
pygame.init()

size = width, height = 600, 700

# 创建指定大小的窗口
screen = pygame.display.set_mode(size)
# 设置窗口标题
pygame.display.set_caption("初次见面，请大家多多关照！")

f = open("record.txt", "w")

while True:
    for event in pygame.event.get():
        f.write(str(event) + "\n")

        if event.type == pygame.QUIT:
            f.close()
            sys.exit()

