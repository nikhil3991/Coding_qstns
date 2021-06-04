import sys
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix) -> int:
        # [rows, columns] = binaryMatrix.dimensions()
        rows = len(binaryMatrix)
        columns = len(binaryMatrix[0])
        ans = sys.maxsize
        for i in range(rows):
            low = 0
            high = columns - 1

            while low <= high:
                mid = (low + high) // 2
                print(i,mid)
                temp = binaryMatrix[i][mid]
                if temp == 1:
                    ans = min(ans, mid)
                    high =mid - 1
                else:
                    low = mid + 1
        if ans == sys.maxsize:
            print(-1)
        else:
            print(ans)
A= [[1,1,1,1,1],[0,0,0,1,1],[0,0,1,1,1],[0,0,0,0,1],[0,0,0,0,0]]
s=Solution()
s.leftMostColumnWithOne(A)