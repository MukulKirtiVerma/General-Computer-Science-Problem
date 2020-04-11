# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 11:49:46 2020

@author: Mukul Kirti Verma
"""

def knapsack(w,wt,v,n):
    if(w==0 or n==0):
        return 0
    elif(wt[n-1]>w):
        knapsack(w,wt,v,n-1)
    else:
        return max(v[n-1]+knapsack(w-wt[n-1],wt,v,n-1),knapsack(w,wt,v,n-1))
v = [60, 100, 120] 
wt = [10, 20, 30] 
w = 50
n = len(v) 
print(knapsack(w, wt, v, n)) 