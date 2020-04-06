# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 01:26:17 2020

@author: Mukul Kirti Verma
"""

s=[(4, 6), (1, 2), (4, 5), (10, 12)]
c,i=0,0
while(i<len(s)-1):
   c+=max(abs(s[i][0]-s[i+1][0]),abs(s[i][1]-s[i+1][1]))
   i+=1
print(c)