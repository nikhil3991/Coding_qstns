from Tress import Basics
class Node:
    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None
        self.sum = 0

class Solution:
    def count(self, root):
        if root is None:
            return 0
        L = self.count(root.left)
        R = self.count(root.right)
        root.s = root.val + L + R
        return root.s

    def maxSumBST(self, root):
        if root is None:
            return 0
        temp = self.count(root)

        def utility(root, mini, maxi):

            if root is None:
                return True
            if (mini != None and root.val <= mini) or (maxi != None and root.val >= maxi):
                return
            if utility(root.left, mini, root.val) and utility(root.right, root.val, maxi):
                self.ans = max(self.ans, root.s)
                # print(root.s)
                return True
            else:
                return False
        def preorder(root):
            if root is None:
                return
            utility(root,None,None)
            preorder(root.left)
            preorder(root.right)

        self.ans = -999999
        preorder(root)
        # utility(root, None, None)
        print(self.ans)
T=Basics.Tree()
T.addNode(1)
T.addNode(4)
T.addNode(3)
T.addNode(2)
T.addNode(4)
T.addNode(2)
T.addNode(5)
T.root.right.right.left = Node(4)
T.root.right.right.right = Node(6)
s= Solution()
s.maxSumBST(T.root)