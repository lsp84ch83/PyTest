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

size = width, height = 600, 400
# 创建指定大小的窗口
screen = pygame.display.set_mode(size)
# 设置窗口标题
pygame.display.set_caption("初次见面，请大家多多关照！")
bg = (0, 0, 0)

font = pygame.font.Font(None, 20)
line_height = font.get_linesize()
position = 0


screen.fill(bg)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


        screen.blit(font.render(str(event), True, (0, 255, 0)), (0, position))
        position += line_height

        if position > height:
            position = 0
            screen.fill(bg)

    pygame.display.flip()