from Tress import Basics
from Linkedlists import Basics

def Allsequences(root):
    result = []
    if root is None:
        result.append([])
        return result
    prefix = []
    prefix.append(root.value)
    print(prefix)

    left = Allsequences(root.left)
    right = Allsequences(root.right)


    for i in left:
        for j in right:
            weaved = []
            weaved = weavelists(i,j,weaved,prefix)
            if weaved is not None:
                for i in weaved:
                    result.append(i)


    return result



def weavelists(first,second,results,prefix):
    if len(first) == 0 or len(second) == 0:
        result = prefix
        # print(result)
        for i in first:
            result.append(i)
        for i in second:
            result.append(i)
        for i in result:
            results.append(i)
        return results

    temp1 = first.pop(0)
    prefix.append(temp1)
    weavelists(first,second,results,prefix)
    prefix.pop()
    first.insert(0,temp1)

    temp2 = second.pop(0)
    prefix.append(temp2)
    weavelists(first,second,results,prefix)
    prefix.pop()
    second.insert(0,temp2)





T = Basics.Tree()
T.addNode(30)
T.addNode(20)
T.addNode(40)
T.addNode(19)
T.addNode(25)
T.addNode(36)
T.addNode(45)
T.inorder(T.root)
print(Allsequences(T.root))