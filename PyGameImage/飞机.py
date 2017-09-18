# -*- coding:utf-8 -*-

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((450,800),0,32)
pygame.display.set_caption('飞机')
bg = pygame.image.load('back.jpg').convert()
plane = pygame.image.load('plane.png').convert_alpha()
bullet = pygame.image.load('bullet.png').convert_alpha()

#  加载子弹
bullet_x = 0
bullet_y = -1

#  初始化子弹位置
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            pygame.quit()
            exit()
    screen.blit(bg,(0,0))
    x,y = pygame.mouse.get_pos()
    if bullet_y < 0:
        #  如果子弹位置超出了屏幕上端
        bullet_x = x - bullet.get_width()/2
        bullet_y = y - bullet.get_height()/2
        #  把子弹的中心位置设为鼠标坐标
    else:
        bullet_y -= 5
        #  把子弹的位置往上移
    screen.blit(bullet,(bullet_x,bullet_y))
    #  把子弹画到屏幕上
    x -= plane.get_width()/2
    y -= plane.get_height()/2
    screen.blit(plane,(x,y))
    pygame.display.update()
