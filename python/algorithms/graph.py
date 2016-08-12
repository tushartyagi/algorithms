import pdb


class Edge:

    def __init__(self, v1, v2):
        self._vertices = (v1, v2)
        for vertex in self.vertices():
            vertex.add_edge(self)

    def vertices(self):
        return self._vertices

    def update(self, v1, v2):
        self._vertices = (v1, v2)

    def __str__(self):
        v1 = self.vertices()[0]
        v2 = self.vertices()[1]
        return "Edge({0},{1})".format(v1.name(), v2.name()) 

    __repr__ = __str__

    
class Vertex:

    def __init__(self, name, edges=None):
        self._name = name
        if edges is not None:
            self._edges = edges
        else:
            self._edges = [] 

    def name(self):
        return self._name
        
    def weighted(self):
        pass

    def weight(self):
        pass

    def edges(self):
        return self._edges

    def add_edge(self, e):
        self._edges.append(e)

    def __str__(self):
        return "Vertex({0})".format(self.name())

    __repr__ = __str__

    
# Adjacency list representation
class Graph:

    def __init__(self):
        self._adj_list = {}


    
