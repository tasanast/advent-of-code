def get_node(name, parent_folder, node_type, size=0):
    node = {
                'name': name,
                'parent_folder': parent_folder,
                'node_type': node_type,
                'size': size
            }

    return node
