# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 19:20:59 2020

@author: Mukul Kirti Verma
"""

arr=[1,1,2,-1,4,5,45]
k=5
if(min(arr)>=0):
    print(sum(arr))
else:
    mx=-999999999
    i=0
    j=1
    start=0
    end=0
    su=arr[0]
    count=0
    while(i+k<len(arr)+1):
        
        su=sum(arr[i:i+k])
        if(su>mx):
            mx=su
            print(arr[i:i+k])
           
        i+=1
    print(mx)
        