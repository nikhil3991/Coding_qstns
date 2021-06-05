from Tress import Basics as N

def addNodeBst(arr,start,end):
    if end < start:
        return None
    mid = (start+end)//2
    temp = N.Node(arr[mid])
    temp.left = addNodeBst(arr,start,mid-1)
    temp.right = addNodeBst(arr,mid+1,end)
    return temp



T = N.Tree()
print(T.root)
arr = [1,2,3,4,5,6,7]
T.root = addNodeBst(arr,0,len(arr)-1)
print(T.root.value)
print("-"*40)
T.inorder(T.root)