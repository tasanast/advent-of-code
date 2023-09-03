# adventofcode.com 2022 day99

import sys
from node_template import get_node 

data = []

def main(input_filename):
    with open(input_filename) as file:
        line = file.readline()
        while line:
            data.append(line.strip())
            line = file.readline()

    for line in data:
        words = line.split(" ")

        if words[0] == "$":
            if words [1] == "cd":
                current_directory = words[2]
                parrent_directory = 



if __name__ == "__main__":
    main(sys.argv[1])
