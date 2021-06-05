from Tress import Basics

class Node:
    def __init__(self,data = None):
        self.value =data
        self.left=None
        self.right = None
        self.diameter = 0

def height(root):
    if root is None:
        return 0
    left = height(root.left)
    right = height(root.right)
    root.diameter = 1+left+right
    global maximum
    if maximum < root.diameter:
        maximum = root.diameter
        global temp
        temp = root

    return 1+max(left,right)

def printutility(root):
    if root is None:
        return
    print(root.value)
    if root.left is None and root.right is None:
        return
    if root.left is None:
        printutility(root.right)
    elif root.right is None:
        printutility(root.left)
    else:
        if root.left.diameter < root.right.diameter:
            printutility(root.right)
        else:
            printutility(root.left)


def printpath(temp):
    print(temp.value)
    printutility(temp.left)
    printutility(temp.right)


def diameter(root):
    if root is None:
        return
    # temp =None
    ht = height(root)
    # path =[]
    printpath(temp)


T = Basics.Tree()
T.addNode(1)
T.addNode(2)
T.addNode(3)
T.addNode(4)
T.addNode(5)
T.root.left.left.right = Node(8)
T.root.left.left.right.left = Node(9)
T.root.left.right.left = Node(6)
T.root.left.right.right = Node(7)
temp = Node()
maximum =0
diameter(T.root)