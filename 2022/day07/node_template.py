class Node:
    """Node representing a file or a folder"""

    def __init__(self, name, size=0):
        self.size = size
        self.parent_folder = None
        self.children = []
        self.total_size = None
        self.name = name

    def get_size(self):
        if self.total_size == None:
            self.total_size = self.size
            for node in self.children:
                self.total_size += node.get_size()

        return self.total_size

    def add_child(self, child_node):
        child_node.parent_folder = self
        self.children.append(child_node)

    def cd(self, directory_name):
        destination_directory = None
        if directory_name == "..":
            destination_directory = self.parent_folder

        # find child directory
        for node in self.children:
            if node.name == directory_name:
                destination_directory = node

        return destination_directory

    def is_folder(self):
        return len(self.children) != 0
            
