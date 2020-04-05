# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:15:08 2020

@author: Mukul Kirti Verma
"""

# A simple Python program for traversal of a linked list 

# Node class 
class Node: 
	def __init__(self, data): 
		self.data = data 
		self.next = None

#create LinkedList(Empty)
l1=Node('')

def insert(ll):
    temp=ll
    while(temp.next!=None):
        temp=temp.next
    x=input('enter data')
    while(x!='exit'):
        x=input('enter data or type exit to exit: ')
        temp.next=Node(x)
        temp=temp.next
        
    return ll

def print_ll(ll):
    temp=ll
    while(temp.next!=None):
        print(temp.data)
        temp=temp.next
def delete(ll):
    

l2=Node('')
l2=insert(l2)
print_ll(l2)