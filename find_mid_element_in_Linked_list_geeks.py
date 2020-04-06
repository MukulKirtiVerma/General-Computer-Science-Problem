# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:24:53 2020

@author: Mukul Kirti Verma
"""

# your task is to complete this function
# function should return index to the any valid peak element
def findMid(head):
    # Code here
    temp=head
    temp2=head
    if(head==None):
        
        return temp
    else:
        while(temp.next!=None):
            temp=temp.next
            if(temp.next!=None):
                temp=temp.next
            temp2=temp2.next
    return temp2

    
     


#{ 
#  Driver Code Starts
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
        else:
            new_node = node(val)
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node

def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head = createList(arr, n)
        print(findMid(head).data)




# } Driver Code Ends