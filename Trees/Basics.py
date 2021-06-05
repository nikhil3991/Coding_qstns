class Node:
    def __init__(self,data = None):
        self.value = data
        self.left = None
        self.right = None
        self.count=0


class Tree:

    def __init__(self):
        self.root = None


    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.value)
        self.inorder(root.right)

    def preorder(self,root):
        if root is None:
            return
        print(root.value)
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self,root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.value)

    def height(self,root):
        if root is None:
            return 0
        lheight = self.height(root.left)
        rheight = self.height(root.right)
        if rheight > lheight:
            return rheight+1
        else:
            return lheight+1

        # return max(lheight,rheight)+1

    def addNode(self,val):
        if self.root is None:
            self.root = Node(val)
            return
        temp = self.root
        queue = []
        queue.append(temp)
        while queue:
            n = queue.pop(0)
            if n.left == None:
                n.left = Node(val)
                return
            else:
                queue.append(n.left)

            if n.right == None:
                n.right = Node(val)
                return
            else:
                queue.append(n.right)










