# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 13:29:24 2020

@author: Mukul Kirti Verma
"""
"""
procedure insertionSort( A : array of items )
   int holePosition
   int valueToInsert
	
   for i = 1 to length(A) inclusive do:
	
      /* select value to be inserted */
      valueToInsert = A[i]
      holePosition = i
      
      /*locate hole position for the element to be inserted */
		
      while holePosition > 0 and A[holePosition-1] > valueToInsert do:
         A[holePosition] = A[holePosition-1]
         holePosition = holePosition -1
      end while
		
      /* insert the number at hole position */
      A[holePosition] = valueToInsert
      
   end for
	
end procedure
"""
def rearrange(arr,j):
    while j>0:
        if(arr[j]<arr[j-1]):
            arr[j]=arr[j]^arr[j-1]
            arr[j-1]=arr[j]^arr[j-1]
            arr[j]=arr[j]^arr[j-1]
            print(arr)
        else:
            break
        j-=1
    return arr

def insertion(arr):
    i=0
    while(i+1<len(arr)):
        if(arr[i]>arr[i+1]):
            arr=rearrange(arr,i+1)            
        i+=1
insertion([1,-2,5,6,-1])
        
        
        
        
        
        
        
        
        
        
        
        
        