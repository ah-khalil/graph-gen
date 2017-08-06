from graphics import *

class Node(Circle):
        def __init__(self, centre, radius, name : str):
            self.name = name
            self.centre = centre
            self.radius = radius
            self.connections = {}
            super().__init__(centre, radius)

        def __hash__(self):
            return hash((self.name, self.centre, self.radius))

        def __eq__(self, other):
            return (self.name, self.centre, self.radius) == (other.name, other.centre, other.radius)

        def __ne__(self, other):
            return not(self == other)

        def get_name(self):
            return self.name

        def get_centre(self):
            return self.centre

        def get_radius(self):
            return self.radius

        def add_connection(self, node, con_point):
            self.connections[node] = con_point

        def check_conn(self, node):
            return (node in self.connections)

        def get_con_point(self, node):
            if self.check_conn(node):
                return self.connections[node]
            else:
                print("{} not connected to {}".format(str(node.get_name()), self.name))

        def get_connection_amount(self):
            return len(self.connections)

        def draw_node(self, window):
            super().draw(window)

        #can't place resize function here as it involves the destruction of the object and a reconstruction using the init function

