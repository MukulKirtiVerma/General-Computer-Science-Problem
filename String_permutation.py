# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 01:01:37 2020

@author: Mukul Kirti Verma
"""
def permu(st,l,r):
    if(l>=r):
        print(''.join(st))
    else:
        for i in range(l,r):
            st[l],st[i]=st[i],st[l]
            permu(st,l+1,r)
            st[l],st[i]=st[i],st[l]

s="asd"
permu(list(s),0,len(s))
