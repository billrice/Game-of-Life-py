#MATRIX

##billx=10
##billy=10


def naberb(posb,billx,billy):
    #for k in matrixb.keys():
    k=posb
    #print (k)
    kidx={}
    kidx['klu']=(k[0]-1,k[1]-1)
    kidx['klm']=(k[0]-1,k[1])
    kidx['kld']=(k[0]-1,k[1]+1)
    kidx['kmu']=(k[0],k[1]-1)
    #kmm=(k[0],k[1])
    kidx['kmd']=(k[0],k[1]+1)
    kidx['kru']=(k[0]+1,k[1]-1)
    kidx['krm']=(k[0]+1,k[1])
    kidx['krd']=(k[0]+1,k[1]+1)
    kidxf={}
    for kid in kidx.keys():
        if not(kidx[kid][0]==-1 or kidx[kid][0]==billx or  kidx[kid][1]==-1 or kidx[kid][1]==billy):
            kidxf[kid]=kidx[kid]
    return kidxf


