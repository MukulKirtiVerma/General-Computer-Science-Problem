# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 00:54:05 2020

@author: Mukul Kirti Verma
"""

#code
t=int(input())
import numpy as np
def ch(x,y):
    try:
        mat[x][y]
        if(x<0 or y<0):
            return False
        return True
    except:
       
            
        return False
def fun(x,y,t,z):
    if(ch(x,y)!=True):
        return
    
    if(mat[x][y]==t):
        mat[x][y]=z
        fun(x-1,y,t,z)
        fun(x,y-1,t,z)
        fun(x+1,y,t,z)
        fun(x,y+1,t,z)
    else:
        return
mat=[]
while t:
    z=input().split()
    x,y=int(z[0]),int(z[1])
    mat=list(np.asarray(input().split(),dtype='int').reshape(x,y))
    for i in range(len(mat)):
        mat[i]=list(mat[i])
    z=input().split()

    xx,yy,zz=int(z[0]),int(z[1]),int(z[2])
    fun(xx,yy,mat[xx][yy],zz)
    for i in range(len(mat)):
        for j in range(y):
            print(mat[i][j],end=" ")
    print()
    t-=1