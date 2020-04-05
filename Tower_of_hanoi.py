# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 20:41:58 2020

@author: Mukul Kirti Verma
"""

def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        print("move from",fromPole,"to",toPole)
        moveTower(height-1,withPole,toPole,fromPole)
moveTower(3,"a","b","c")