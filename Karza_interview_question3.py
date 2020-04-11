# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 19:02:54 2020

@author: Mukul Kirti Verma
"""

arr=[1,2,5,1,6,6,6,6,6]
a=set(arr)
l=[]
lenth=len(arr)/2
for i in a:
    l.append((i,arr.count(i)))
for i in l:
    if(i[1]>=lenth):
        print(i[0])