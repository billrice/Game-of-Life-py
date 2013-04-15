#!/usr/bin/env python
 
import pygame
from pygame.locals import *
from sys import exit

 
from random import *


pygame.init()
screen = pygame.display.set_mode((840, 680), 0, 32)
pygame.display.set_caption("burberry")
points = []

intb=9

##while True:
 
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            exit()
##        if event.type == KEYDOWN:
##            # 按任意键可以清屏并把点回复到原始状态
##            points = []
##            screen.fill((255,255,255))
##        if event.type == MOUSEBUTTONDOWN:
##            screen.fill((255,255,255))
##            
##        # 获得当前鼠标点击位置
##    ##        x, y = pygame.mouse.get_pos()
##    ##        points.append((x, y))
##        
        # 从左上和右下画两根线连接到点击位置
for i in range(840//intb):
    pygame.draw.line(screen, (0, 0, 0), (i*intb, 0), (i*intb, 480))
for j in range(680//intb):
    pygame.draw.line(screen, (0, 0, 0), (0,j*intb), (640,j*intb))

##          把每个点画明显一点
##            for p in points:
##                pygame.draw.circle(screen, (155, 155, 155), p, 3)
for i in range(840//intb):
    for j in range(680//intb):
        pygame.draw.circle(screen, (int(random()*255), int(random()*255), int(random()*255)), (i*intb+(intb//2+1),j*intb+(intb//2+1)), (intb//2))

        
## 
pygame.display.update()
