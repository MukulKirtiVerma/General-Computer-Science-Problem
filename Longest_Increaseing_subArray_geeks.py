# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 19:51:56 2020

@author: Mukul Kirti Verma
"""


t=int(input())
for tt in range(t):
    n=int(input())
    arr=[int(i) for i in input().split()]
    a=[1]*n
    i=0
    j=1
    for i in range(1,n):
        for j in range(0,i+1):
            if(arr[i]>arr[j] and a[i]<=a[j]):
                a[i]=a[i]+1
    print(max(a))
    