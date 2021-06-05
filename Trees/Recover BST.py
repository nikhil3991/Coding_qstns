from Tress import  Basics
class Solution:
    def __init__(self):
        self.temp1=None
        self.temp2 = None
        self.prev = Basics.Node(float('-inf'))
    # @param A : root node of tree
    # @return a list of integers
    def traverse(self,temp):
        if temp is None:
            return
        self.traverse(temp.left)
        if temp.value <= self.prev.value:
            if self.temp1 is None:
                self.temp1 = self.prev
            if self.temp1:
                self.temp2 = temp
        self.prev = temp
        self.traverse(temp.right)

    def recoverTree(self, A):
        if A is None:
            print(195)
            return
        self.traverse(A)
        return [self.temp1.value,self.temp2.value]

T1= Basics.Tree()
T1.addNode(1)
T1.addNode(2)
T1.addNode(3)
T1.inorder(T1.root)
s=Solution()
print(s.recoverTree(T1.root))



