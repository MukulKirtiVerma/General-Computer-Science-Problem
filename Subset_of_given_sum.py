# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 13:42:22 2020

@author: Mukul Kirti Verma
"""
#ok
arr=[2,3,3,5,6]
i=0
j=1
s=5
ss=arr[0]
while(i!=j and j<len(arr)):
    if(ss>s):
        ss=ss-arr[i]
        i+=1
        
    elif(ss<s):
       j+=1
    if(ss==s):
        print(arr[i:j])
        i=i+1
        j=i+2
        ss=arr[i]
    
    
    