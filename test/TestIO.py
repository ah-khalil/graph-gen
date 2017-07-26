from unittest import TestCase
import sys
sys.path.append('..')
from src.fileio.reader import create_vertex_list
import pprint

class TestIo(TestCase):
    def test_arrow_case(self):
        test_str = "A (B, 2), (C, 7), (D, 8)"
        expected_error = "Make sure the node name and it's adjacent nodes are separated by a '->"

        self.assertion_check(expected_error, test_str)

    def test_no_data(self):
        test_str = "A -> "
        expected_error = "If there are nodes that aren't connected to anything, don't add an arrow"

        self.assertion_check(expected_error, test_str)

    def test_extra_data(self):
        test_str = "A -> (B, 2, 4)"
        expected_error = "Too much data, use only name and distance"

        self.assertion_check(expected_error, test_str)

    def test_non_number(self):
        test_str = "A -> (B, p)"
        expected_error = "Distance should be a number"

        self.assertion_check(expected_error, test_str)

    def assertion_check(self, expected_error, test_str):
        with self.assertRaises(IOError) as context:
            create_vertex_list(test_str)

        self.assertIn(expected_error, str(context.exception))

    def test_correct_input(self):
        test_str = "A -> (B, 2), (C, 7), (D, 8)"
        expected_result = {'A': {'B': 2.0, 'C': 7.0, 'D': 8.0}}
        actual_result = create_vertex_list(test_str)

        # pp = pprint.PrettyPrinter()
        # pp.pprint(actual_result)

        for node in expected_result:
            self.assertIn(node, actual_result)
            for adj_node in expected_result[node]:
                self.assertIn(adj_node, actual_result[node])

