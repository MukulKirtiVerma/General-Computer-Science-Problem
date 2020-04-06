# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 17:20:49 2020

@author: Mukul Kirti Verma
"""
n=11# nth ugly no.
l=[1]
n1=2
nc1=2
n2=3
nc2=2
n3=5
nc3=2
c=1
i=1
count=1
while i:
    if(n1<=n2 and n1<=n3):
        c=n1
        n1=2*nc1
        nc1+=1
        
        
    elif(n2<=n1 and n2<=n3):
        c=n2
        n2=3*nc2
        nc2+=1
    elif(n3<=n1 and n3<=n1):
        c=n3
        n3=5*nc3
        nc3+=1
    if(count==n):
        print(c)
        i=0  
    count+=1
    
