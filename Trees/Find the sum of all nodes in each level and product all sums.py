from Tress import Basics

def findsum(root,hd,level):
    if root is None:
        return
    try:
        hd[level]+=root.value
    except:
        hd[level] = root.value

    findsum(root.left,hd,level+1)
    findsum(root.right,hd,level+1)

def findproduct(root):
    hd ={}
    findsum(root,hd,0)
    res=1
    for i in hd.keys():
        res*=hd[i]
    print(res)


T=Basics.Tree()
T.root = Basics.Node(1)
T.addNode(2)
T.addNode(3)
T.addNode(4)
T.addNode(5)
T.addNode(6)
T.addNode(7)
T.addNode(8)
T.addNode(2)
findproduct(T.root)