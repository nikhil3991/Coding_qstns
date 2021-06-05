from Tress import Basics
class Solution:
    def sumNumbers(self, root) -> int:
        if root is None:
            return 0
        def utility(root):
            if root is None:
                return
            self.ans*=10
            self.ans+=root.val
            print(self.ans)
            utility(root.left)
            utility(root.right)
            if root.left is None and root.right is None:
                self.count+=self.ans
            self.ans//=10
        self.ans = 0
        self.count = 0
        utility(root)
        print(self.count)
T=Basics.Tree()
T.addNode(1)
T.addNode(2)
T.addNode(3)
s = Solution()
s.sumNumbers(T.root)