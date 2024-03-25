class Node:
    def __init__(self,root):
        self.root=root
        self.left=None
        self.right=None
class tree:
    def preorder(self,root):
        if root is not None:
            print(root.root)
            self.preorder(root.left)
            self.preorder(root.right)

root=Node(10)
root.left=Node(9)
root.right=Node(11)
root.left.left=Node(8)
root.left.right=Node(10)
root.right.left=Node(12)
root.right.right=Node(22)
pre_ord=tree()
pre_ord.preorder(root)