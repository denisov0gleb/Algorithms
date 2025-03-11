class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def search_recursively(self, root, node):
        if node is None or node.data == node:
            return node
        elif node.data > node:
            return self.search_recursively(node.left, node)
        else:
            return self.search_recursively(node.rigth, node)
        
    def insert_node(self, node, node_data):
        if node is None:
            node = Node(node_data)
        else:
            if node.data > node_data:
                node.left = self.insert_node(node.left, node_data)
            elif node.data < node_data:
                node.right = self.insert_node(node.right, node_data)
        return node

    def find_min(self, node):
        if node.left is not None:
            return self.find_min(node.left)
        else:
            return node

    def delete_recursively(self, node, node_data):
        if node is None:
            return None
        
        if node.data > node_data:
            node.left = self.delete_recursively(node.left, node_data)
            return node
        elif node.data < node_data:
            node.right = self.delete_recursively(node.right, node_data)
            return node

        if node.left is None:
            return node.right
        elif node.right is None:
            return node.right
        else:
            min_data = self.find_min(node.right).data
            node.data = min_data
            node.right = self.delete_recursively(node.right, min_data)
            return node

    def print_tree(self, node, level=0):
        if node != None:
            self.print_tree(node.right, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.data))
            self.print_tree(node.left, level + 1)


if __name__ == "__main__":
    tree = Tree()
    tree.root = tree.insert_node(tree.root, 3)
    tree.root = tree.insert_node(tree.root, 7)
    tree.root = tree.insert_node(tree.root, 10)
    tree.root = tree.insert_node(tree.root, 2)
    tree.root = tree.insert_node(tree.root, 4)
    tree.root = tree.insert_node(tree.root, 5)
    tree.root = tree.insert_node(tree.root, 1)

    # tree.root = tree.delete_recursively(tree.root, 4)
    tree.print_tree(tree.root)