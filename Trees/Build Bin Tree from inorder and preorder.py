class Nodes:
    def __init__(self,data=None):
        self.value = data
        self.right = None
        self.left = None

# start,end is for inorder array
def buildtree(inorder,preorder,start,end):
    if (start > end):
        return None
    temp = Nodes(preorder[buildtree.preindex])
    buildtree.preindex+=1
    if start == end:
        return temp
    inIndex = search(inorder,start,end,temp.value)

    temp.left = buildtree(inorder,preorder,start,inIndex-1)
    temp.right = buildtree(inorder,preorder,inIndex+1,end)
    return temp

def search(arr,start,end,value):
    for i in range(start,end+1):
        if arr[i] == value:
            return i


def inorder1(root):
    if root is None:
        return
    inorder1(root.left)
    print(root.value)
    inorder1(root.right)







inorder = ["D","B","E","A","F","C"]
preorder = ["A","B","D","E","C","F"]
buildtree.preindex = 0
root = buildtree(inorder,preorder,0,len(inorder)-1)
inorder1(root)
print("-"*40)
