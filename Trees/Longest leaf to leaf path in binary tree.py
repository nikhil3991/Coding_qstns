from Tress import Basics
class Node:
    def __init__(self,data = None):
        self.value =data
        self.left=None
        self.right = None

def height(root,lh,rh,ans,temp):
    if root is None:
        return 0
    left = height(root.left,lh,rh,ans,temp)
    right = height(root.right,lh,rh,ans,temp)
    if ans < (1 + left + right):
        ans = 1+left+right
        temp = root
        lh = left
        rh =right
    return max(left,right)+1

def printpath(path,len,f):
    if f==0:
        for i in range(len-1,-1,-1):
            print(path[i])
    elif f==1:
        for i in range(len):
            print(path[i])


def printrecur(root,var,path,pathlen,f):
    if root is None:
        return
    path[pathlen] = root.value
    pathlen+=1
    if root.left is None and root.right is None:
        if pathlen == var and (f==0 or f==1):
            printpath(path)
            f=2
        else:
            printrecur(root.left,ans,path,pathlen,f)
            printrecur(root.rigt,ans,path,pathlen,f)








def diameter(root):
    if root is None:
        return None
    # lpath = []
    # rpath =[]
    # pathlen =0
    # f=0
    # lh =0
    # rh=0
    # temp = 0
    h_tree = height(root,lh,rh,ans,temp)
    f=0
    printrecur(temp.left,lh,lpath,pathlen,f)
    print(temp.value)
    f=1
    printrecur(temp.right,rh,rpath,pathlen,f)





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
# T.inorder(T.root)
lpath = []
rpath =[]
pathlen =0
f=0
lh =0
rh=0
temp = Node()
ans =0
diameter(T.root)






