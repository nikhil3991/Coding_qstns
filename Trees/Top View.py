from Tress import Basics
def Solve(root):
    if root is None:
        return None
    temp = {}
    def utility(node,height,hd):
        if node is None:
            return  None
        if hd not in temp:
            temp[hd] = [node.value,height]
        else:

            x = temp[hd][1]
            if x>height:
                temp[hd] = [node.value,height]
        utility(node.left,height+1,hd-1)
        utility(node.right,height+1,hd+1)
    utility(root,0,0)
    for i in sorted(temp.keys()):
        print(temp[i][0])


T=Basics.Tree()
T.root = Basics.Node(1)
T.addNode(2)
T.addNode(3)
T.addNode(4)
T.addNode(5)
T.addNode(6)
T.addNode(7)
T.root.left.left.right= Basics.Node(10)
T.root.left.left.right.right = Basics.Node(11)
T.root.left.left.right.right.right = Basics.Node(12)
Solve(T.root)