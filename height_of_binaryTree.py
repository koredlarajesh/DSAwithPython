class Node:
    def __init__(self,root):
        self.root=root
        self.left=None
        self.right=None
class tree:
    def height(self,root):
        if root is None:
            return 0
        else:
            lh=self.height(root.left)
            rh=self.height(root.right)
            return max(lh,rh)+1


node1 = Node(12)
node2 = Node(10)
node3 = Node(15)
node4 = Node(20)

# Constructing tree structure
node1.left = node2
node1.right = node3
node3.left = node4
# Creating tree object
binary_tree = tree()

# Performing inorder traversal
print(binary_tree.height(node1))
