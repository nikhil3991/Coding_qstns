class Node:
    def __init__(self,data = None):
        self.value = data
        self.left = None
        self.right = None

# def totalNodes(root):
#     if root is None:
#         return 0
#     return 1 + totalNodes(root.left) + totalNodes(root.right)


def covers(root,p):
    if root is None:
        return False
    if root == p:
        return True
    return covers(root.left,p) or covers(root.right,p)

def ancestorHelper(root,p,q):
    if root == None or root ==p or root ==q:
        return root
    pleft = covers(root.left,p)
    qleft = covers(root.left,q)
    if pleft!=qleft:
        return root
    if pleft:
        childside = root.left
    else:
        childside = root.right
    return ancestorHelper(childside,p,q)

def commonAncestor(root,p,q):
    if (not covers(root,p) or not covers(root,q)):
        return None
    return ancestorHelper(root,p,q)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
a=commonAncestor(root,root.left.left,root.left.right)
print(a.value)
