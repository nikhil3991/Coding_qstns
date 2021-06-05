from Tress import Basics


class LinkedNode:
    def __init__(self,data=None):
        self.value = data
        self.next = None

def add(root,temp):
    NewNode = LinkedNode(temp)
    NewNode.next = root
    return NewNode


def createLL(root,st,depth):
    if root is None:
        return
    if st[depth]:
        st[depth] = add(st[depth],root.value)
    else:
        st[depth] = LinkedNode(root.value)

    if root.left:
        createLL(root.left,st,depth+1)
    if root.right:
        createLL(root.right,st,depth+1)

    return st


T = Basics.Tree()
T.root = Basics.Node(1)
T.addNode(2)
T.addNode(3)
T.addNode(4)
T.addNode(5)
T.addNode(6)
T.addNode(7)
T.addNode(8)
T.addNode(9)
height = T.height(T.root)
stack = [None]*height

res =createLL(T.root,stack,0)
for temp in res:
    # temp = i
    while temp:
        print(temp.value,end = ' ')
        temp = temp.next

    print("")




