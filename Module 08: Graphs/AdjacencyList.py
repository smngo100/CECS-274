"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack


class AdjacencyList(Graph):
    def __init__(self, n : int):
        self.n = n    # number of nodes 
        self.adj = np.zeros(n, object)
        for i in range(self.n):
            self.adj[i] = ArrayList.ArrayList()
            
    def add_edge(self, i : int, j : int):
        # todo        # add the edge (i, j) to E    
        pass

    def remove_edge(self, i : int, j : int):
        # todo        # remove the edge (i, j) from E 
        pass
                
    def has_edge(self, i : int, j: int) ->bool:
        # todo        # returns true if the edge (i, j) exists in E 
        pass
        
    def out_edges(self, i) -> List:
        # todo        # returns a list of all integers j such that (i, j) ∈ E 
        pass

    def in_edges(self, i) -> List:
        # todo        # returns a list of all integers i such that (i, j) ∈ E 
        pass
    
    def bfs(self, r : int, dest: int):
        traversal = []    # empty list to store the vertices in the order that they are visited
        seen = [] # Boolean values 
        q = []    # empty queue to keep track of the vertices for which we must visit neighbors

       q.append(i)
       traversal.append(i)
       seen[i] = True 

       while q is not None:
           current = q.remove()    # temp variable
           neighbors = current    # temp variable

            for 

    def dfs(self, r : int, dest: int):
        # todo
        pass    
                    
    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s
