# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:07:21 2020

@author: Mukul Kirti Verma
"""

arr=[4,7,4,3,3,5,6,8,5,3,2,4,6,78,6,3]
search_element=2
result='not found'
for i in arr:
    if(i==search_element):
        result=i
        print('found at',i)
        break
if(result=='not found'):
    print(result)