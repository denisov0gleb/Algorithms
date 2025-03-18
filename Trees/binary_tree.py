class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


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
        return self.balance(root)

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

    def _height(self, node):
        return node.height if node else 0
    
    def _fix_height(self, node):
        node.height = max(self._height(node.left), self._height(node.right)) + 1

    def _balance_factor(self, root):
        return self._height(root.right) - self._height(root.left)


    def _rotate_right(self, pivot_node):
        next_parent = pivot_node.left
        pivot_node.left = next_parent.right
        next_parent.right = pivot_node
        self._fix_height(pivot_node)
        self._fix_height(next_parent)
        return next_parent

    def _rotate_left(self, pivot_node):
        next_parent = pivot_node.right
        pivot_node.right = next_parent.left
        next_parent.left = pivot_node
        self._fix_height(pivot_node)
        self._fix_height(next_parent)
        return next_parent

    def balance(self, pivot_node):
        self._fix_height(pivot_node)
        if self._balance_factor(pivot_node) == 2:
            if self._balance_factor(pivot_node.right) < 0:
                pivot_node.right = self._rotate_right(pivot_node.right) # if big rotation is needed (clockwise -> counter clockwise)
            return self._rotate_left(pivot_node)
        
        elif self._balance_factor(pivot_node) == -2:
            if self._balance_factor(pivot_node.left) > 0:
                pivot_node.left = self._rotate_left(pivot_node.left)
            return self._rotate_right(pivot_node)
        
        return pivot_node # no balance is needed


if __name__ == "__main__":
    tree = Tree()
    tree.root = tree.insert_node(tree.root, 5)
    tree.root = tree.insert_node(tree.root, 3)
    tree.root = tree.insert_node(tree.root, 6)
    tree.root = tree.insert_node(tree.root, 2)
    tree.root = tree.insert_node(tree.root, 1)
    tree.root = tree.insert_node(tree.root, 0)
    tree.root = tree.insert_node(tree.root, 7)
    tree.root = tree.insert_node(tree.root, 4)

    tree.root = tree.delete_recursively(tree.root, 4)
    tree.print_tree(tree.root)