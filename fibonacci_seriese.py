# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 20:58:11 2020

@author: Mukul Kirti Verma
"""

x=int(input('enter total no of element to be print: '))
n1=1
n2=1
if(x==1):
    print(1)
elif(x==2):
    print(1,1)
else:
    print(n1)
    print(n2)
    x=x-2
    while x:
        print(n1+n2)
        temp=n1+n2
        n1=n2
        n2=temp
        x-=1
        
