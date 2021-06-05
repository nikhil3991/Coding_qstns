from Tress import Basics
import sys

class Node:
    def __init__(self,data=None):
        self.value = data
        self.left = None
        self.right = None

def checkheight(root):
    if root is None:
        return -1
    lh = checkheight(root.left)
    rh = checkheight(root.right)
    if abs(lh -rh)>1:
        print("False")
        return -1
    else:
        return max(lh,rh)+1

def height(root):
    if root is None:
        return -1
    return max(height(root.left),height(root.right))+1

def checkBalanced(root):
    if root is None:
        return True
    hd = height(root.left) - height(root.right)
    if abs(hd)>1:
        return False
    else:
        return checkBalanced(root.left) and checkBalanced(root.right)






T = Basics.Tree()
T.root = Node(1)
T.addNode(2)
T.addNode(3)
T.addNode(4)
T.addNode(5)
T.root.left.left.left = Node(6)
T.inorder(T.root)
print(checkBalanced(T.root))
print(checkheight(T.root))