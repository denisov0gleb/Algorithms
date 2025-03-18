class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def search_recursively(self, root, node_data):
        if root is None or root.data == node_data:
            return root
        elif root.data > node_data:
            return self.search_recursively(root.left, node_data)
        else:
            return self.search_recursively(root.rigth, node_data)
        
    def insert_node(self, root, node_data):
        if root is None:
            root = Node(node_data)
        else:
            if root.data > node_data:
                root.left = self.insert_node(root.left, node_data)
            elif root.data < node_data:
                root.right = self.insert_node(root.right, node_data)
        return root

    def find_min(self, root):
        if root.left is not None:
            return self.find_min(root.left)
        else:
            return root

    def delete_recursively(self, root, node_data):
        if root is None:
            return None
        
        if root.data > node_data:
            root.left = self.delete_recursively(root.left, node_data)
            return root
        elif root.data < node_data:
            root.right = self.delete_recursively(root.right, node_data)
            return root

        if root.left is None:
            return root.right
        elif root.right is None:
            return root.right
        else:
            min_data = self.find_min(root.right).data
            root.data = min_data
            root.right = self.delete_recursively(root.right, min_data)
            return root

    def print_tree(self, root, level=0):
        if root != None:
            self.print_tree(root.right, level + 1)
            print(' ' * 4 * level + '-> ' + str(root.data))
            self.print_tree(root.left, level + 1)


if __name__ == "__main__":
    tree = Tree()
    tree.root = tree.insert_node(tree.root, 3)
    tree.root = tree.insert_node(tree.root, 7)
    tree.root = tree.insert_node(tree.root, 10)
    tree.root = tree.insert_node(tree.root, 2)
    tree.root = tree.insert_node(tree.root, 4)
    tree.root = tree.insert_node(tree.root, 5)
    tree.root = tree.insert_node(tree.root, 1)
    tree.root = tree.insert_node(tree.root, 0)

    tree.root = tree.delete_recursively(tree.root, 4)
    tree.print_tree(tree.root)