# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 23:18:06 2020

@author: Mukul Kirti Verma
"""

l=[]
n,k=3,3
n,k=n+1,k+1

for i in range(n):
   l.append([0]*(k))
i=0
for i in range(1,n):
    for j in range(1,k):
        if(j==1 or j==i):
            l[i][j]=1
        else:
            l[i][j]=l[i-1][j-1]+l[i-1][j]*j
print(l[i][j])
        