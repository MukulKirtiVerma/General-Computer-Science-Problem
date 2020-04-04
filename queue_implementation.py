# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:58:00 2020

@author: Mukul Kirti Verma
"""

queue = [] 

queue.append('a') 
queue.append('b') 
queue.append('c') 
  
print("Initial queue") 
print(queue) 
try:
    print(queue.pop(0)) 
    print(queue.pop(0)) 
    print(queue.pop(0)) 
except:
    print('no element in queue to pop')
#
print("\nQueue after removing elements") 
print(queue) 
  