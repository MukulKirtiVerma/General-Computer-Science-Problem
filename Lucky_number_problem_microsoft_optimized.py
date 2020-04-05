# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 18:47:43 2020

@author: Mukul Kirti Verma
"""

def islucky(n):
    global count
    if(count>n):
        return 1
    if(n%count==0):
        return 0
    np=n
    np=np-np//count
    count+=1
    return islucky(np)

t=int(input())

while t:
    count=2
    temp=int(input())
    x=islucky(temp)
    print(x)
    t-=1
    
    
    
