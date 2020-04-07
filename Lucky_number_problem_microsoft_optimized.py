# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 18:47:43 2020

@author: Mukul Kirti Verma
"""

def islucky(n):
    global count
    print(n,count)
    if(count>n):
        print('count>n')
        return 1
    
    if(n%count==0):
        print('count>n')
        return 0
    np=n
    np=np-np//count
    count+=1
    return islucky(np)

count=2
islucky(19)
    
    
    
