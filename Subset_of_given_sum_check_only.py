

# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 01:52:09 2020

@author: Mukul Kirti Verma
"""

arr=[2,3,6]# array
s=10#  Given sum


arr.insert(0,0)
l=len(arr)
dp=[]
for i in range(l):
    d=[]
    for j in range(s+1):
        if( j==0):
            d.append(True)
        else:
            d.append(False)
    dp.append(d)

for i in range(1,l):
    for j in range(1,s+1):
        
        if(arr[i]==j or (dp[i-1][j]==True and i!=1)):
            print(arr[i],j)
            dp[i][j]=True
        else:
            t=j-arr[i]
            if(t<0):
                continue
            if(dp[i-1][t]==True):
                dp[i][j]=True
            else:
                dp[i][j]=False
print(dp[i][j])