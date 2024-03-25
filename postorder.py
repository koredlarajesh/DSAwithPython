class Node:
    def __init__(self,root):
        self.root=root
        self.left=None
        self.right=None
class tree:
    def postorder(self,root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.root)

root=Node(10)
root.left=Node(9)
root.right=Node(11)
root.left.left=Node(8)
root.left.right=Node(10)
root.right.left=Node(12)
root.right.right=Node(22)
post_ord=tree()
post_ord.postorder(root)