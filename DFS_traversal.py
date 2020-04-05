# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 20:39:46 2020

@author: Mukul Kirti Verma
"""



graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E','A'],
  'C' : ['F','A'],
  'D' : ['B'],
  'E' : ['F','B'],
  'F' : ['C','E']
}

visited = [] # List to keep track of visited nodes.
Stack = []     #Initialize a Stack

def bfs(visited, graph, node):
  visited.append(node)
  Stack.append(node)

  while Stack:
    s = Stack.pop() 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        Stack.append(neighbour)

# Driver Code
bfs(visited, graph, 'A') 