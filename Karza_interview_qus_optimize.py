# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 14:16:34 2020

@author: Mukul Kirti Verma
"""

arr=[1,1,2,-100,4,5,45,9]
k=5
i=0
mx=-99999999
j=1
su=arr[0]
count=1
while(j<len(arr)):
    #print(count,k,j)
    if(count>k-1): 
        
        su=su-arr[i]+arr[j]
        if(su>mx):
            mx=su
        i+=1
    else:
        su=su+arr[j]
        
        count+=1
    print(mx)
    j+=1
print(mx)
        