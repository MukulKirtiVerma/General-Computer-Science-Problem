# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:18:29 2020

@author: Mukul Kirti Verma
"""
def merg(arr1,arr2):
    arr1.append(99999999999)#add max number
    arr2.append(99999999999)
    k,l=0,0
    arr=[]
    while(k<len(arr1)-1 or l<len(arr2)-1):
        if(arr1[k]>=arr2[l]):
            arr.append(arr2[l])
            l+=1
        else:
            arr.append(arr1[k])
            k+=1
    return arr
def merg_sort(array):
    if(len(array)<=1):
        return array
    else:
        arr1=array[0:len(array)//2]
        arr2=array[(len(array)//2):len(array)]
        #print(arr1,'\n',arr2)
        l1=merg_sort(arr1)
        l2=merg_sort(arr2)
        return merg(l1,l2)
x=[1,2000,3,8,9,11,-1,12,23,24,25,55,66,88,99,2]#input less then 99999999999
merg_sort(x)
    