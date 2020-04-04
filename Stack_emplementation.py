# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:00:08 2020

@author: Mukul Kirti Verma
"""
stack = [] 
#puch fuction
stack.append('a')#like push function 
stack.append('b') 
stack.append('c') 
  
print('Initial stack') 
print(stack) 
#pop fuction
try:
    print(stack.pop()) 
    print(stack.pop()) 
    print(stack.pop()) 
except:
    print('no element in stack') 
#peak function
x=max(stack)
print(x)