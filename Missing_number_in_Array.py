# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 16:55:03 2020

@author: Mukul Kirti Verma
"""
# just past code in geeks to relevent problem and run

arr=[1,2,4,5]
c=0
for i in range(1,len(arr)):
    c=c^i
cc=0
for i in arr:
    cc=cc^int(i)
print(c^cc)
    