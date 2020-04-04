# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 15:19:27 2020

@author: Mukul Kirti Verma
"""
def partition(array, start, end):
    pivot = array[start]
    l = start + 1
    h = end
    while True:
        while l <= h and array[h] >= pivot:
            h = h - 1
        while l <= h and array[l] <= pivot:
            l = l + 1
        if l <= h:
            array[l] =array[h]
            array[h] =array[l]
        else:
            break
    array[start]=array[h]
    array[h] =array[start]
    return h

def quick_sort(array, start, end):
    if start >= end:
        return
    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)
array = [5,9,8,9,0]

quick_sort(array, 0, len(array) - 1)
print(array)