class Nodes:
    def __init__(self,data=None):
        self.value = data
        self.right = None
        self.left = None

class BinTree:
    def __init__(self):
        self.root = None
    # Inorder traversal of Binary Tree
    def inorder(self,temp):
        if temp == None:
            return
        self.inorder(temp.left)
        print(temp.value)
        self.inorder(temp.right)
    #
    # Inserting a Node into a binary tree in level order
    def insertion(self,data,temp):
        if temp is None:
            self.root = Nodes(data)
            return
        items = []
        items.insert(0,temp)
        while items:
            curr = items[len(items)-1]
            items.pop()
            if curr.left ==None:
                curr.left = Nodes(data)
                return
            else:
                items.insert(0,curr.left)
            if curr.right == None:
                curr.right = Nodes(data)
                return
            else:
                items.insert(0,curr.right)

    def spiral(self,root):
        if root is None:
            return
        currlevel = []
        nextlevel = []
        bool=True
        currlevel.insert(0,root)
        while len(currlevel)>0:
            temp=currlevel.pop(-1)
            print(temp.value,end = '')
            if bool:
                if temp.left:
                    nextlevel.append(temp.left)
                if temp.right:
                    nextlevel.append(temp.right)
            else:
                if temp.right:
                    nextlevel.append(temp.right)
                if temp.left:
                    nextlevel.append(temp.left)

            if len(currlevel)==0:
                bool = not bool
                currlevel,nextlevel = nextlevel,currlevel





    def zigzag(self,root):
        if root is None:
            return
        currlevel = []
        nextlevel = []
        bool = False
        currlevel.insert(0,root)
        while len(currlevel)>0:
            temp=currlevel.pop(-1)
            print(temp.value,end = '')
            if bool:
                if temp.left:
                    nextlevel.append(temp.left)
                if temp.right:
                    nextlevel.append(temp.right)
            else:
                if temp.right:
                    nextlevel.append(temp.right)
                if temp.left:
                    nextlevel.append(temp.left)

            if len(currlevel)==0:
                bool = not bool
                currlevel,nextlevel = nextlevel,currlevel


T1 = BinTree()
T1.root = Nodes(1)
T1.root.left = Nodes(2)
T1.root.right = Nodes(3)
# T1.root.left.left = Nodes(7)
# T1.root.right.left = Nodes(15)
# T1.root.right.right = Nodes(8)
T1.insertion(4,T1.root)
T1.insertion(5,T1.root)
T1.insertion(6,T1.root)
T1.insertion(7,T1.root)
T1.inorder(T1.root)
print("-"*40)
T1.spiral(T1.root)
print("-"*40)
T1.zigzag(T1.root)