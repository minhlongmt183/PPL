class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def count(root):
    if root is None:
        return 0
    else:
        return 1 + count(root.left) + count(root.right)

def sum(root):
    l = sum(root.left) if root.left else 0
    r = sum(root.right) if root.right else 0
    return root.val + (sum(root.left) if root.left else 0) + (sum(root.right) if root.right else 0)
    
ex = Node(3,Node(4,Node(5)),Node(10))  
print(count(ex))
print(sum(ex))