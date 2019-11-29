# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 19:55:26 2019

@author: hp
"""

x=[1,1,3,1,2,3,3,2,7,3,1,7,1,2,3,4,15,26,2,2,3,1,1,2,36,6,7]
maax=0;
temp=0;
temp2=0
maax2=9999
i=0
while i<len(x)-1:
    
    if(i%2==0):
        temp+=x[i]
        if(temp>maax):
            maax=temp  
        if(temp<maax2):
            maax2=temp
        
    else:
        
        temp-=x[i]
        if(temp>maax):
                maax=temp  
        if(temp<maax2):
                maax2=temp
        
        
    if(temp>maax):
        maax=temp
    else:
        maax2
    print(temp)
    i=i+1
maax2=-1*maax2
xy=[]
for i in range(maax+maax2+5):
    xz=[]
    for j in range(sum(x)+1):
        xz.append(" ")
    xy.append(xz)
h=len(xy)-maax2-1
w=0
for i in range(len(x)):
    if(i%2==0):
        for i in range(x[i]):
            print(h,w)
            xy[h][w]='/'
            w+=1
            h-=1
        h+=1
    else:
        
      for i in range(x[i]):
            print(h,w)

            xy[h][w]=r'\\'
            w+=1
            h+=1
      h=h-1

for i in xy:
    st=""
    for j in i:
            if(j==r"\\"):
                st+=j
                st=st[:-1]
            else:
                st+=j
    print(st)
        







