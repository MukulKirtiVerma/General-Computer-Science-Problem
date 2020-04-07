# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 20:37:43 2020

@author: Mukul Kirti Verma
"""

#code
tt=int(input())
for t in range(tt):
    nm=input().split()
    n,m=int(nm[0]),int(nm[1])
    x1=[0]+list(input())
    x2=[0]+list(input())
    #ok
    dp=[]
    for i in range(len(x1)):
        d=[]
        for j in range(len(x2)):
            d.append(0)
        dp.append(d)
    mx=0
    for i in range(1,len(x1)):
        for j in range(1,len(x2)):
            if(x1[i]==x2[j]):
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                
    print(dp[i][j])
           
            