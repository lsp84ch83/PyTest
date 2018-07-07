# _*_ coding:utf-8 _*_
# 多图点击循环切换,有缺陷，可能会多次随机到同一张图

from sys import exit
import pygame
import random
from pygame import *



#  初始化PyGame
pygame.init()
#  创建一个窗口，窗口大小和背景图片一样
screen = pygame.display.set_mode((600,177),0,32)
#  设置窗口标题
pygame.display.set_caption('植物大战僵尸')
#  加载并转换背景图片
background1 = image.load('PyGame.gif').convert()
background2 = image.load('Pygame_New.jpg ').convert()
background3 = image.load('zwjs.jpg').convert()
bgimg = [background1,background2,background3]
target = True
background = background1

#  主循环
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == MOUSEBUTTONDOWN:
            #  接收鼠标按下事件后更换背景
            background = random.choice(bgimg)
    #  将背景图画上去
    screen.blit(background,(0,0))
    #  刷新画面
    pygame.display.update()
