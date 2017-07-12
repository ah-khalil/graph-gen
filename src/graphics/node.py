from graphics import *
from copy import deepcopy

class Node(Circle):
    def __init__(self, vertex, centre_xy, radius):
        self.name = vertex.get_name()
        self.degree_points = {}
        self.vertex = vertex
        super.__init__(centre_xy, radius)

    def get_vertex_copy(self):
        return deepcopy(vertex)
