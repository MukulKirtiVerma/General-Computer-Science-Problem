# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 20:09:53 2020

@author: Mukul Kirti Verma
"""
#time complexity =O(n)
#space complexity =O(max(n,max(arr)))
 
arr=[1,2,5,1,6,6,6,6,6]
a=[0]*max(max(arr),len(arr))
for i in arr:
    a[i]+=1

for i in a:
    if(i>=len(arr)/2):
        print(arr[i])