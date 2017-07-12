import re
from collections import defaultdict

def read_file(path):
    with open(path) as f:
        lines = f.readlines()

    vertex_list = defaultdict(lambda: 'NA')

    for node_input in lines:
        lines = node_input.strip("\n")
        lines_arr = lines.split("->")
        regex = '[A-Z],\s[0-9]'
        items = re.findall(regex, lines_arr[1])

        sub_dict = {}
        for adj in items:
            adj_dist = adj.split(", ")
            sub_dict[adj_dist[0]] = int(adj_dist[1])

        vertex_list[lines_arr[0].strip()] = sub_dict

    """for x in vertex_list:
        print(x)
        for y in vertex_list[x]:
            print ("\t" + y, ":", vertex_list[x][y])"""

    return vertex_list    
