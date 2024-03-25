class Node:
    def __init__(self,root):
        self.root=root
        self.left=None
        self.right=None
class tree:
    def inorder(self,root,left,right):
        if Node is not None:
            self.inorder(Node.left)
            print(Node.root)
            self.inorder(Node.right)
node1 = Node(12)
node2 = Node(10)
node3 = Node(15)

# Constructing tree structure
node1.left = node2
node1.right = node3

# Creating tree object
binary_tree = tree()

# Performing inorder traversal
binary_tree.inorder(node1)

