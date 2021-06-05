from Tress import Basics


def match(temp1,temp2):
    if temp1 == None and temp2 == None:
        return True
    if temp1 == None or temp2 == None:
        return False
    if temp1.value != temp2.value:
        return False
    else:
        return match(temp1.left,temp2.left) and match(temp1.right,temp2.right)

def wrapper(temp1,temp2):
    if temp1 == None:
        return False
    if temp1.value == temp2.value and match(temp1,temp2):
        return True
    else:
        return wrapper(temp1.left,temp2) or wrapper(temp1.right,temp2)



def subTree(temp1,temp2):
    if temp2 is None:
        return True
    return wrapper(temp1,temp2)




T1 = Basics.Tree()
T1.root = Basics.Node(1)
T1.addNode(2)
T1.addNode(3)
T1.addNode(4)
T1.addNode(5)
T1.addNode(6)
T1.addNode(7)
T1.addNode(8)
T1.addNode(9)
T1.addNode(10)
T1.addNode(11)
T1.addNode(12)
T1.addNode(13)
T1.addNode(14)
T1.addNode(15)
T1.addNode(16)
T1.addNode(17)
T1.addNode(18)


T2 = Basics.Tree()
T2.root = Basics.Node(4)
T2.addNode(8)
T2.addNode(9)
T2.addNode(16)
T2.addNode(17)
T2.addNode(18)

print(subTree(T1.root,T2.root))




