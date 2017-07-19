import sys
sys.path.append('..')
from src.fileio.reader import read_file
from collections import defaultdict
from pprint import PrettyPrinter

#this script tests to see if the structure of the dictionary is readable and the
#necessary information is easily accessible

#unenforcable consts
SMALLEST_SINGLE_PATH = 2
LONGEST_SINGLE_PATH = 8
VERT_NUM = 6

distance_dict = defaultdict(dict)
pp = PrettyPrinter()

def test_input_structure(path):
    try:
        read_file(path)
    except IOError as err:
        print("IO Error: {0}".format(err))

def distance_calc():
    for node in range(VERT_NUM):
        current_letter = chr(ord('A') + node)
        print("Current Letter: " + current_letter)
        for adj_node in range(VERT_NUM):
            current_adj_node = chr(ord('A') + adj_node)
            print("\tcurrent adjacent letter: " + current_adj_node)
            if current_adj_node is not current_letter:
                distance_dict[current_letter][current_adj_node] = gaussian_sum(current_letter, current_adj_node)
                pp.pprint(distance_dict[current_letter])
            else:
                print("Same as current letter")

def gaussian_sum(starting_letter, terminal_letter):
    a_range = ord(starting_letter) - 65 + 1
    b_range = ord(terminal_letter) - 65 + 1
    g_sum = abs((b_range * (b_range + 1) - a_range * (a_range + 1)) / 2)

    print("\t\t" + starting_letter + "->" + terminal_letter + ":")
    print("\t\t\tA-Range: " + str(a_range))
    print("\t\t\tB-Range: " + str(b_range))
    print("\t\t\tG-Sum: " + str(g_sum))

    return g_sum

def set_dest(path):
    vertex_list = read_file(path)
    for source in vertex_list:
        print("Source: " + source)
        for destination in vertex_list:
            if source != destination:
                print("\tDestination: " + destination)
                create_path(source, destination, vertex_list, 0, [])

def create_path(subject_node, dest_node, vertex_dict, distance_sum, discovered):
    discovered.append(subject_node)
    if subject_node == dest_node:
        print("\t\tCompleted, distance: " + str(distance_sum))
        return True

    found_flag = False
    for adj_node in vertex_dict[subject_node]:
        if found_flag:
            break
        if adj_node not in discovered:
            distance_to_node = vertex_dict[subject_node][adj_node]
            print("\t\t\t" + subject_node + "->" + adj_node + ", " + str(distance_to_node))

            found_flag = create_path(adj_node, dest_node, vertex_dict, distance_sum + distance_to_node, discovered)

    return found_flag

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: dictionary_test.py INPUT\n\nVisualizes an input graph.\n\npositional arguments:\nFILE:\ta path to the graph file, relative to the current path")
    else:
        distance_calc()
        print("======================================TEST: CORRECT INPUT FILE======================================\n")
        set_dest(sys.argv[1])
        print("====================================================================================================\n")

        print("======================================TEST: INCORRECT INPUT FILE; NO ARROW==========================\n")
        test_input_structure(sys.argv[2])
        print("====================================================================================================\n")
