# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 13:22:06 2020

@author: Mukul Kirti Verma
"""

def bubble(arr):
    for i in range(len(arr)):
        j,k,l=0,1,len(arr)-1
        swap=False
        while(j!=l):
            
            if(arr[j]>arr[k]):
                arr[j]=arr[j]^arr[k]
                arr[k]=arr[j]^arr[k]
                arr[j]=arr[j]^arr[k]
                swap=True
            j+=1
            k+=1
        l-=1
        if(swap==False):
            break
    return arr
x=[2,9,-13,6,4,1,5,8,9,100]#input
bubble(x)
        