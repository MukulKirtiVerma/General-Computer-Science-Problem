# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 18:50:49 2020

@author: Mukul Kirti Verma
"""

n=5  
n=n+1
c=[1]*n

for i in range(2,n):
    c[i]=0
    for j in range(0,i):
       c[i]=c[i]+c[j]*c[i-j-1]
print(c[n-1])
