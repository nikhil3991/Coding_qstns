from Tress import Basics

def iterPreorder(root):
    if root is None:
        return
    stack = []
    stack.append(root)
    while stack:
        temp = stack.pop(-1)
        print(temp.value)
        if temp.right:
            stack.append(temp.right)
        if temp.left:
            stack.append(temp.left)

def iterInorder(root):
    if root is None:
        return
    stack =[]
    temp = root
    while True:
        if temp is not None:
            stack.append(temp)
            temp=temp.left
        elif stack:
            temp = stack.pop()
            print(temp.value,end=' ')
            temp = temp.right
        else:
            break

def iterPostorder1(root):
    if root is None:
        return
    stack1 = []
    stack2 = []
    stack1.append(root)
    while stack1:
        temp = stack1.pop()
        stack2.append(temp)
        if temp.left:
            stack1.append(temp.left)
        if temp.right:
            stack1.append(temp.right)
    while stack2:
        curr =stack2.pop()
        print(curr.value)

def iterPostorder2(root):
    if root is None:
        return
    stack =[]
    res=[]
    # curr = root
    while True:
        while root is not None:
            stack.append(root)
            stack.append(root)
            root=root.left
        if len(stack)<=0:
            print(res)
            return
        root = stack.pop()
        if (len(stack)>0 and stack[-1] == root):
            root = root.right
        else:
            print(root.value, end = ' ')
            res.append(root.value)

            root = None











T = Basics.Tree()
T.root = Basics.Node(1)
T.addNode(2)
T.addNode(3)
T.addNode(4)
T.addNode(5)
T.addNode(6)
T.addNode(7)
T.root.left.right.left = Basics.Node(8)
# T.postorder(T.root)
print("-"*50)
iterPostorder2(T.root)
print("-"*50)
