import re
from collections import defaultdict


#   Opens a file stream to the path indicated in the import and reads lines
#   :param path:
#   :return lines:
def read_file(path):
    with open(path) as f:
        lines = f.readlines()

    return lines

#   Creates a dictionary with the vertices in the input file
#   :param in_line:
#   :return vertex_list:

def create_vertex_list(in_line):
    vertex_list = defaultdict(lambda: 'NA')

    lines = in_line.strip("\n")
    lines_arr = lines.split("->")

    if len(lines_arr) != 2:
        raise IOError("Make sure the node name and it's adjacent nodes are separated by a '->")

    #the following is quite ugly, will be optimized later
    regex_number = '[A-Z],\s[0-9]'
    regex_non_number = '[A-Z],\s.'
    regex_all = '[A-Z](,\s.){2,}'

    items = re.findall(regex_number, lines_arr[1])

    if len(items) == 0:
        if len(re.findall(regex_non_number, lines_arr[1])) == 0:
            raise IOError("If there are nodes that aren't connected to anything, don't add an arrow")
        elif len(re.findall(regex_non_number, lines_arr[1])) > 0:
            raise IOError("Distance should be a number")
    elif len(re.findall(regex_all, lines_arr[1])) > 0:
        raise IOError("Too much data, use only name and distance")

    sub_dict = {}
    for adj in items:
        adj_dist = adj.split(',')
        sub_dict[adj_dist[0]] = float(adj_dist[1].strip(" "))

    vertex_list[lines_arr[0].strip()] = sub_dict

    return vertex_list
