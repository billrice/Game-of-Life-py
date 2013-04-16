import matrix


matrixbnext={}

def changeb(matrixb,billx,billy):
    for i in matrixb.keys():
        countb=0
        
        #当前为空的格子，如果周围有三个非空=>变非空
        if matrixb[i][0]==0:
            listb=[0,0,0]
            #kidx返回周围坐标点
            for kidx in matrix.naberb(i,billx,billy).values():
                #周围非空时+1
                #print (matrixb[kidx])
                try:
                    if matrixb[kidx][0]==1:
                        countb=countb+1
                        #周围点颜色matrixb[kidx][1]
                        listb[0]=listb[0]+matrixb[kidx][1][0]
                        listb[1]=listb[1]+matrixb[kidx][1][1]
                        listb[2]=listb[2]+matrixb[kidx][1][2]
                        #print(listb)
                except:
                    print (matrixb)
                    print (kidx)
            if countb==3:
                
                for j in range(3):
                    listb[j]=listb[j]//3 - 20*j
                print(listb)
                listb=tuple(listb)
                matrixbnext[i]=(1,listb)
                #matrixbnext[i]=(1,(255,255,255))
                
            else:
                matrixbnext[i]=(0,(255,255,255))
        #当前为非空的格子，如果周围有2/3个非空=>保持
        elif matrixb[i][0]==1:
            for kidx in matrix.naberb(i,billx,billy).values():
               if matrixb[kidx][0]==1:
                   countb=countb+1
            if countb==2 or countb==3:
                matrixbnext[i]=(1,(255,255,255))
            else:
                matrixbnext[i]=(0,(255,255,255))
    return matrixbnext
