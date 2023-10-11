class Node:
    parent_folder = None
    children = []
    size = 0

    def __init__(self, size):
        self.size = size

    def get_size(self):
        total_size = self.size
        for node in children:
            size += node.get_size()

        return total_size

    def add_child(child_node):
        childrent.append(child_node)
