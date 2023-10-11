# adventofcode.com 2022 day07 part 1

import sys
from node_template import Node

def get_sum(max_size, parent_node):
    total_sum = 0
    if parent_node.is_folder():
        if parent_node.get_size() <= max_size:
            total_sum += parent_node.get_size()
        for node in parent_node.children:
            total_sum += get_sum(max_size, node)
    return total_sum

data = []
root_folder = Node("/")

def main(input_filename):
    with open(input_filename) as file:
        line = file.readline()
        while line:
            data.append(line.strip())
            line = file.readline()
    
    # Build folder tree

    current_folder = root_folder
    for line in data:
        words = line.split(" ")
        
        # Handle commands 
        if words[0] == "$":
            if words [1] == "cd":
                if words[2] == "/":
                    current_folder = root_folder
                else:
                    current_folder = current_folder.cd(words[2])

        # add children to current folder
        elif words[0] == "dir":
            current_folder.add_child(Node(words[1]))
        else: 
        # add file to the children list
            current_folder.add_child(Node(words[1], int(words[0])))

    # get sum
    print(get_sum(100000,root_folder))
    


if __name__ == "__main__":
    main(sys.argv[1])
