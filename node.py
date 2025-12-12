class node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def preorder(root):
    if root != None:
        preorder(root.left)
        print(root.data)
        preorder(root.right)

root = node('a')
root.left = node('b')
root.right = node('c')
root.left.right = node('f')
root.left.right.left = node('g')
root.left.right.right = node('h') 
preorder(root)