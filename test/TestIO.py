from unittest import TestCase
import sys
sys.path.append('..')
from src.fileio.reader import create_vertex_list

class TestIo(TestCase):
    def test_no_name(self):
        test_str = "-> (B, 2), (C, 7), (D, 8)"
        expected_error = "Make sure the node name and it's adjacent nodes exist and are separated by a '->'"

        self.assertion_check(expected_error, test_str)

    def test_arrow_case(self):
        test_str = "A (B, 2), (C, 7), (D, 8)"
        expected_error = "Make sure the node name and it's adjacent nodes exist and are separated by a '->'"

        self.assertion_check(expected_error, test_str)

    def test_no_data(self):
        test_str = "A -> "
        expected_error = "Make sure the node name and it's adjacent nodes exist and are separated by a '->'"

        self.assertion_check(expected_error, test_str)

    def test_extra_data(self):
        test_str = "A -> (B, 2, 4)"
        expected_error = "Too much data, use only name and distance"

        self.assertion_check(expected_error, test_str)

    def test_non_number(self):
        test_str = "A -> (B, p)"
        expected_error = "Distance should be a number"

        self.assertion_check(expected_error, test_str)

    def test_correct_input(self):
        test_str = "A -> (B, 2), (C, 7), (D, 8)"
        expected_result = {'A': {'B': 2.0, 'C': 7.0, 'D': 8.0}}
        actual_result = create_vertex_list(test_str)
        self.assertion_check_correct(expected_result, actual_result)

    def test_empty_input(self):
        test_str = " "
        expected_error = "Make sure the node name and it's adjacent nodes exist and are separated by a '->'"

        self.assertion_check(expected_error, test_str)

    def test_multiple_lines(self):
        test_str = "A -> (B, 2), (C, 7), (D, 8)\nB -> (A, 2), (C, 3)\nC -> (A, 7), (B, 3), (D, 4)\nD -> (A, 8), (C, 4), (E, 5)\nE -> (C, 4), (D, 5), (F, 6)\nF -> (E, 6)"
        test_arr = test_str.split("\n")
        expected_result = {'A': {'B': 2.0, 'C': 7.0, 'D': 8.0}, 'B': {'A': 2, 'C': 3}, 'C': {'A': 7, 'B': 3, 'D': 4}, 'D': {'A': 8, 'C': 4, 'E': 5}, 'E': {'C': 4, 'D': 5, 'F': 6}, 'F': {'E': 6}}

        for line in test_arr:
            actual_result = create_vertex_list(line)
            self.assertion_check_correct(expected_result, actual_result)

    def assertion_check(self, expected_error, test_str):
        with self.assertRaises(IOError) as context:
            create_vertex_list(test_str)

        self.assertIn(expected_error, str(context.exception))

    def assertion_check_correct(self, expected_result, actual_result):
        for node in actual_result:
            self.assertIn(node, expected_result)
            for adj_node in actual_result[node]:
                self.assertIn(adj_node, expected_result[node])
