##For a space that is 'populated':
##Each cell with one or no neighbors dies, as if by loneliness.
##Each cell with four or more neighbors dies, as if by overpopulation.
##Each cell with two or three neighbors survives.
##For a space that is 'empty' or 'unpopulated'
##Each cell with three neighbors becomes populated.


import matrix
import random

import pygame
from pygame.locals import *
from sys import exit
import time

billx=10
billy=10

billr=10

matrixb={}
matrixbnext={}

for i in range(billx):
    for j in range(billy):
        matrixb[(i,j)]=int(random.random()*5//3)
        print (matrixb[(i,j)],end="  ")
    print ('\n')



pygame.init()
screen = pygame.display.set_mode((billx*billr*2,billy*billr*2), 0, 32)
pygame.display.set_caption("burberry")
points = []



def changeb(matrixb):
    for i in matrixb.keys():
        countb=0
        if matrixb[i]==0:
            for kidx in matrix.naberb(i,billx,billy).values():
               if matrixb[kidx]==1:
                   countb=countb+1
            if countb==3:
                matrixbnext[i]=1
            else:
                matrixbnext[i]=0
        elif matrixb[i]==1:
            for kidx in matrix.naberb(i,billx,billy).values():
               if matrixb[kidx]==1:
                   countb=countb+1
            if countb==2 or countb==3:
                matrixbnext[i]=1
            else:
                matrixbnext[i]=0
    return matrixbnext

for kk in range(120):
    print ('################')
    billq=changeb(matrixb)    


##    for i in range(billx):
##        for j in range(billy):
##            print (billq[(i,j)],end="  ")
##        print ('\n')
    screen.fill((0,0,0))
    for i in range(billx):
        pygame.draw.line(screen, (0, 0, 0), (i*billr*2, 0), (i*billr*2, billy*billr*2))
    for j in range(billy):
        pygame.draw.line(screen, (0, 0, 0), (0,j*billr*2), (billx*billr*2,j*billr*2))
    

    for i in matrixb.keys():
        if matrixb[i]==1:
            pygame.draw.circle(screen, (255,255,255), (i[0]*billr*2+billr,i[1]*billr*2+billr), billr)

    pygame.display.update()
    matrixb=billq
    time.sleep(1)
            

        

 


    
