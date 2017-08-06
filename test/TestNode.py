from unittest import TestCase
from src.graphics.node import Node
from graphics import Point

class TestNode(TestCase):

    a_centre = Point(600, 600)
    a_radius = 60
    a_name = "Testing Node A"
    node_a = Node(a_centre, a_radius, a_name)

    additional_nodes = []
    additional_points = []
    stack_num = 0
    last_chrnum = 97

    def test_get_name(self):
        self.assertEquals(self.node_a.get_name(), self.a_name)

    def test_get_centre(self):
        self.assertEquals(self.node_a.get_centre(), self.a_centre)

    def test_get_radius(self):
        self.assertEquals(self.node_a.get_radius(), self.a_radius)

    def create_new_node(self):
        multiplier = self.stack_num + 1
        centre = Point(600 * multiplier, 600 * multiplier)
        radius = 60 * multiplier
        xloc = 30 * multiplier
        yloc = 40 * multiplier
        name = 'Testing Node ' + chr(self.last_chrnum)

        self.additional_nodes.append(Node(centre, radius, name))
        self.additional_points.append(Point(xloc, yloc))
        self.last_chrnum += 1
        self.stack_num += 1

    def test_add_connection(self):
        self.create_new_node()
        self.node_a.add_connection(self.additional_nodes[self.stack_num - 1], self.additional_points[self.stack_num - 1])
        self.assertTrue(self.node_a.check_conn(self.additional_nodes[self.stack_num - 1]))

    def test_get_con_point(self):
        self.create_new_node()
        self.node_a.add_connection(self.additional_nodes[self.stack_num - 1], self.additional_points[self.stack_num - 1])
        self.assertEquals(self.additional_points[self.stack_num - 1].getX(),
                          self.node_a.get_con_point(self.additional_nodes[self.stack_num - 1]).getX())
        self.assertEquals(self.additional_points[self.stack_num - 1].getY(),
                          self.node_a.get_con_point(self.additional_nodes[self.stack_num - 1]).getY())

    def test_get_connection_amount(self):
        for nodes in range(0, 10):
            self.create_new_node()
            self.node_a.add_connection(self.additional_nodes[self.stack_num - 1], self.additional_points[self.stack_num - 1])

        self.assertEquals(self.node_a.get_connection_amount(), self.stack_num)

