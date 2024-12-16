from Interfaces import Graph, List
import numpy as np
import ArrayStack
"""An implementation of the adjacency list representation of a graph"""

class AdjacencyMatrix(Graph):

    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros([n,n])

    def add_edge(self, i : int, j : int):
        if 0 <= i and j < self.n:
            self.adj[i][j] = 1

    def remove_edge(self, i : int, j : int):
        if self.adj[i][j] == 1:
            self.adj[i][j] = 0
            return True
        return False

    def has_edge(self, i : int, j: int) ->bool:
        return self.adj[i][j] == 1

    def out_edges(self, i) -> List:
        edges = []
        for j in range(len(self.adj[i])):   # for every entry at column j in row i
            if self.adj[i][j] == 1:
                edges.append(j)
        return edges

    def in_edges(self, j) -> List:
        edges = []
        for i in range(len(self.adj)):   # for every row i at column j
            if self.adj[i][j] == 1:
                edges.append(i)
        return edges

    def bfs(self, r : int):
        traversal = []  # empty list traversal
        seen = [False] * self.n   # empty list seen
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

    def dfs(self, r : int):
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
