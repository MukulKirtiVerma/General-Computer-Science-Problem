# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 20:16:23 2020

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
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
bfs(visited, graph, 'D') 