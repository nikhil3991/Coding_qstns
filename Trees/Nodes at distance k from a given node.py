from Tress import Basics

def printkdistancedown(root,k):
    if root is None or k<0:
        return
    if k==0:
        print(root.value)
        return
    printkdistancedown(root.left,k-1)
    printkdistancedown(root.right,k-1)


def printkdistancenode(root,target,k):
    if root is None:
        return -1
    if root == target:
        printkdistancedown(root,k)
        return 0
    dl =printkdistancenode(root.left,target,k)

    if dl!=-1:
        if dl+1 == k:
            print(root.value)
        else:
            printkdistancedown(root.right,k-dl-2)
        return 1+dl

    dr = printkdistancenode(root.right,target,k)
    if dr!=-1:
        if dr+1==k:
            print(root.value)
        else:
            printkdistancedown(root.left,k-dr-2)
        return 1+dr

    return -1


T=Basics.Tree()
T.root = Basics.Node(20)
T.addNode(8)
T.addNode(22)
T.addNode(4)
T.addNode(12)
T.root.left.right.left = Basics.Node(10)
T.root.left.right.right = Basics.Node(14)
T.inorder(T.root)
print("-"*40)
printkdistancenode(T.root,T.root.right,3)