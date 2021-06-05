import random
class Node:
    def __init__(self,data):
        self.value = data
        self.left = None
        self.right = None
        # self.size = 1

def size(root):
    if root is None:
        return 0
    return 1 + size(root.left) + size(root.right)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.value)
    inorder(root.right)

class Tree:
    def __init__(self):
        self.root = None

def getithNode(d,root):
    if root is None:
        return
    if root.left == None:
        leftsize = 0
    else:
        leftsize = size(root.left)

    if d<=leftsize:
        return getithNode(d,root.left)
    elif d==leftsize +1:
        return root.value
    else:
        return getithNode(d-leftsize-1,root.right)



def getRandomNode(root):
    n = size(root)
    # print(n)
    a= random.randint(1,n)
    print(a)
    return getithNode(a,root)

T = Tree()
T.root = Node(20)
T.root.right = Node(30)
T.root.left = Node(10)
T.root.left.right = Node(15)
T.root.left.right.right = Node(17)
T.root.left.left = Node(5)
T.root.left.left.left = Node(3)
T.root.left.left.right = Node(7)
# inorder(T.root)

print(getRandomNode(T.root))








