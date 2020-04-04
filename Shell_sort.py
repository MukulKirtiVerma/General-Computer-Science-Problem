# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 15:07:16 2020

@author: Mukul Kirti Verma


procedure shellSort()
   A : array of items 
	
   /* calculate interval*/
   while interval < A.length /3 do:
      interval = interval * 3 + 1	    
   end while
   
   while interval > 0 do:

      for outer = interval; outer < A.length; outer ++ do:

      /* select value to be inserted */
      valueToInsert = A[outer]
      inner = outer;

         /*shift element towards right*/
         while inner > interval -1 && A[inner - interval] >= valueToInsert do:
            A[inner] = A[inner - interval]
            inner = inner - interval
         end while

      /* insert the number at hole position */
      A[inner] = valueToInsert

      end for

   /* calculate interval*/
   interval = (interval -1) /3;	  

   end while
   
end procedure
"""

def shellSort(arr): 
    # Start with a big shell, then reduce the shell 
    n = len(arr) 
    shell = n//2

    while shell > 0: 
  
        for i in range(shell,n): 
            temp = arr[i] 
            j = i 
            while  (j >= shell and arr[j-shell] >temp): 
                arr[j] = arr[j-shell] 
                j -= shell 
            arr[j] = temp 
        shell //= 2
    return arr
arr = [ 2,5,8,9,0,2,5,6,8,9]  
print(shellSort(arr))
 