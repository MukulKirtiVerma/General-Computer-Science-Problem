# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:19:26 2020

@author: Mukul Kirti Verma
"""

#code
tt=int(input())
while tt>0:
    n=input()
    n=int(n)
    mx=0
    arr=input().split()
    arr=[int(arr[i]) for i in range(n)]
    if(min(arr)>=0):
        print(sum(arr))
        

    elif(max(arr)<0):
        print(max(arr))
        pass
        
    else:
        s=0
        i=0
        j=0
        mx=-99999999
        idi=0
        idj=0
        while(j<len(arr)):
            s=s+arr[j]
            if(s<0):
                s=0
                i=j+1
                j=j+1
            elif(s>=0):
                if(mx<s):
                    mx=s
                    idi=i
                    idj=j
                j+=1
                
        print(mx)
    tt-=1