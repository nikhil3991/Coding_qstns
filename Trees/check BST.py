from Tress import Basics
class Node:
    def __init__(self,data = None):
        self.value = data
        self.left = None
        self.right = None

def checkBST(root,min,max):
    if root is None:
        return True
    if (min!=None and root.value <= min) or (max!=None and root.value>max):
        return False
    if checkBST(root.left,min,root.value) and checkBST(root.right,root.value,max):
        return True
    else:
        return False


T = Basics.Tree()
T.root = Node(5)
T.addNode(1)
T.addNode(4)
# T.addNode(8)
# T.addNode(25)
# T.root.left.left.left = Node(3)
# T.root.left.left.right = Node(7)

T.root.right.left = Node(3)
T.root.right.right = Node(6)
# T.inorder(T.root)
print("-"*40)
print(checkBST(T.root,None,None))