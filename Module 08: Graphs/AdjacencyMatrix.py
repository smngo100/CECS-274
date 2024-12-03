from Interfaces import Graph, List
import numpy as np
"""An implementation of the adjacency list representation of a graph"""

class AdjacencyMatrix(Graph):

    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros(n*n)

    
    def add_edge(self, i : int, j : int):
        a[i][j] = True    # add the edge (i, j) to E   

    
    def remove_edge(self, i : int, j : int):
        if a[i][j] == 1: 
            a[i][j] = 0
            return True 
        return False
        #a[i][j] = False    # remove the edge (i, j) from E 
    

    def has_edge(self, i : int, j: int) ->bool:
        return a[i][j]    # returns true if the edje (i, j) exists in E 

    
    def out_edges(self, i) -> List:
        # todo        # returns a list of all integers j such that (i, j) ∈ E
        for i in j:
            if a[i][j] == 1: 
                edges.append[j]
        return edges 

    
    def in_edges(self, i) -> List:
        # todo         # returns a list of all integers i such that (i, j) ∈ E
        pass

    
    def bfs(self, r : int):
        # todo
        pass

    
    def dfs(self, r : int):
        # todo
        pass

    
    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s
