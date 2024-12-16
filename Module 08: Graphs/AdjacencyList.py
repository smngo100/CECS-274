"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import ArrayList
import ArrayStack


class AdjacencyList(Graph):
    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros(n, object)
        for i in range(self.n):
            self.adj[i] = ArrayList.ArrayList()
            
    def add_edge(self, i : int, j : int):
        if 0 <= i and j < self.n:
            if j not in self.adj[i]:
                self.adj[i].append(j)

    def remove_edge(self, i : int, j : int):
        if 0 <= i and j < self.n:
            for k in range(len(self.adj[i])):
                if self.adj[i][k] == j:
                    self.adj[i].remove(k)
                    return True
            return False
                
    def has_edge(self, i : int, j: int) ->bool:
        if 0 <= i and j < self.n:
            for k in range(len(self.adj[i])):
                if self.adj[i].get(k) == j:
                    return True
            return False
        
    def out_edges(self, i) -> List:
        if 0 <= i < self.n:
            return self.adj[i]

    def in_edges(self, j) -> List:
        if 0 <= j < self.n:
            incoming = []
            for i in range(self.n):
                if self.has_edge(i, j):
                    incoming.append(i)
            return incoming

    def bfs(self, r : int) -> List:
        traversal = []  # empty list traversal
        seen = [False] * self.n  # empty list seen
        q = []  # empty queue to keep track of the vertices for which we must visit neighbors

        # Visit vertex r
        q.append(r)
        traversal.append(r)
        seen[r] = True

        while q:
            current = q.pop(0)
            neighbors = self.out_edges(current)
            for jk in neighbors:
                if seen[jk] == False:
                    # Visit vertex jk
                    q.append(jk)
                    traversal.append(jk)
                    seen[jk] = True
        return traversal

    def dfs(self, r : int) -> List:
        traversal = []  # empty list traversal
        s = ArrayStack.ArrayStack()
        seen = [False] * self.n
        s.push(r)
        while s.size() > 0:
            current = s.pop()
            if seen[current] == False:
                traversal.append(current)
                seen[current] = True
            neighbors = self.out_edges(current)
            for neighbor in reversed(neighbors):
                if seen[neighbor] == False:
                    s.push(neighbor)
        return traversal

    def size(self):
        return self.n

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s
