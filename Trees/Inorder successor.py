class Node:
    def __init__(self,data = None):
        self.value = data
        self.left = None
        self.right = None
        self.parent = None

def inordersuccessor(root,n):
    if n.right is not None:
        return minvalue(n.right)
    p = n.parent
    while p is not None:
        if n!=p.right:
            break
        n=p
        p=p.parent
    return p


def minvalue(node):
    curr = node
    while curr:
        if curr.left is None:
            break
        curr = curr.left
    return curr



def insert(node, data):
    # 1) If tree is empty then return a new singly node
    if node is None:
        return Node(data)
    else:

        # 2) Otherwise, recur down the tree
        if data <= node.value:
            temp = insert(node.left, data)
            node.left = temp
            temp.parent = node
        else:
            temp = insert(node.right, data)
            node.right = temp
            temp.parent = node

        # return the unchanged node pointer
        return node

root = None
root = insert(root, 20)
root = insert(root, 8);
root = insert(root, 22);
root = insert(root, 4);
root = insert(root, 12);
root = insert(root, 10);
root = insert(root, 14);
temp = root.left
succ = inordersuccessor(root,temp)
if succ:
    print(succ.value)
else:
    print("No Successor")