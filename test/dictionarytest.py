import sys
sys.path.append('..')
from src.fileio.reader import read_file

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
    if len(sys.argv) != 2:
        print("usage: dictionary_test.py INPUT\n\nVisualizes an input graph.\n\npositional arguments:\nFILE:\ta path to the graph file, relative to the current path")
    else:
        set_dest(sys.argv[1])
