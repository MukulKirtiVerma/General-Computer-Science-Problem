# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 14:21:36 2020

@author: Mukul Kirti Verma


procedure selection sort 
   list  : array of items
   n     : size of list

   for i = 1 to n - 1
   /* set current element as minimum*/
      min = i    
  
      /* check the element to be minimum */

      for j = i+1 to n 
         if list[j] < list[min] then
            min = j;
         end if
      end for

      /* swap the minimum element with the current element*/
      if indexMin != i  then
         swap list[min] and list[i]
      end if
   end for
	
end procedure
"""

x=[6,6,2,4,8,5,6,9,0,-1]
j=0
k=0
for i in x:
    x_min=999999999
    j=k
    x_min_id=0
    #find minimum
    while(j<len(x)):
        if(x_min>x[j]):
            x_min=x[j]
            x_min_id=j
        j+=1
    j=k
    #place minimum at correct position
    while(x_min_id>k):
        x[x_min_id]=x[x_min_id-1]
        x_min_id-=1
    x[k]=x_min
    k+=1
    
    
    
    
    
    
    
    
    
    
    
    
    