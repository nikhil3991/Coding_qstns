from Tress import Basics

class Node:
    def __init__(self,data = None):
        self.value = data
        self.left = None
        self.right = None


def prinlist(arr,n):
    for i in range(n,len(arr)):
        print(arr[i],end = ' ')
    print()


def kpathutil(root,path,k):
    if root is None:
        return
    path.append(root.value)
    kpathutil(root.left,path,k)
    kpathutil(root.right,path,k)
    sum =0
    for i in range(len(path)-1,-1,-1):
        sum+=path[i]
        if sum == k:
            # T.count+=1
            prinlist(path,i)

    path.pop()



def kpath(temp,k):
    path = []
    kpathutil(temp,path,k)


T = Basics.Tree()
T.root = Node(10)
T.addNode(5)
T.addNode(-3)
T.addNode(3)
T.addNode(2)
T.root.right.right = Node(11)
T.root.left.left = Node(3)
T.root.left.right.right = Node(1)
T.root.left.left.left = Node(3)
T.root.left.left.right = Node(-2)
# T.inorder(T.root)

kpath(T.root,8)
print("-"*50)
# print(T.count)
