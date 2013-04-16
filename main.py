##For a space that is 'populated':
##Each cell with one or no neighbors dies, as if by loneliness.
##Each cell with four or more neighbors dies, as if by overpopulation.
##Each cell with two or three neighbors survives.
##For a space that is 'empty' or 'unpopulated'
##Each cell with three neighbors becomes populated.

import change
import matrix
import random

import pygame
from pygame.locals import *
from sys import exit
import time

billx=40
billy=40
billr=10

matrixb={}
matrixbnext={}

#初始化点分布矩阵
for i in range(billx):
    for j in range(billy):
        #matrixb[(i,j)]=int(random.random()*100//90)
        #增加每个点的颜色属性
        #初始为(255,255,255)=>白色
        matrixb[(i,j)]=(int(random.random()*100//92),(255,255,255))



#初始化界面
pygame.init()
screen = pygame.display.set_mode((billx*billr*2,billy*billr*2), 0, 32)
pygame.display.set_caption("burberry")
points = []



#变化过程
for kk in range(120):
    print ('################')
    billq=change.changeb(matrixb,billx,billy)    

#黑色背景
    screen.fill((0,0,0))
    for i in range(billx):
        pygame.draw.line(screen, (0, 0, 0), (i*billr*2, 0), (i*billr*2, billy*billr*2))
    for j in range(billy):
        pygame.draw.line(screen, (0, 0, 0), (0,j*billr*2), (billx*billr*2,j*billr*2))
    

    for i in matrixb.keys():
        if matrixb[i][0]==1:
         #   try:
            pygame.draw.circle(screen,matrixb[i][1] , (i[0]*billr*2+billr,i[1]*billr*2+billr), billr)
          #  except:
         #       print (matrixb[i][1])
    pygame.display.update()
    matrixb=billq
    time.sleep(1)
            

        

 


    
