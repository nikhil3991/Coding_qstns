from Tress import Basics

class Node:
    def __init__(self,data = None):
        self.value = data
        self.left = None
        self.right = None

def depth(t,d):
    if t is None:
        return d
    return max(depth(t.left,d+1),depth(t.right,d+1))




T = Basics.Tree()
T.root = Node(1)
T.addNode(2)
T.addNode(3)
T.addNode(4)
T.addNode(5)
T.addNode(6)
T.addNode(7)
T.addNode(8)
T.inorder(T.root)
print("-"*40)
print(depth(T.root,0))
print("-"*40)
print(T.height(T.root))