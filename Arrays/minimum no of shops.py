import sys


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of list of integers
    # @param D : integer
    # @param E : list of list of integers
    # @return an integer
    def solve(self, A, B, C, D, E):
        req = set()
        shops = {}
        m = len(E)
        for i in range(m):
            req.add(E[i][1])
        for i in C:
            if i[1] in req:
                try:
                    shops[i[0]].add(i[1])
                except:
                    shops[i[0]] = set()
                    shops[i[0]].add(i[1])

        ans = sys.maxsize
        for i in range(1, (2 ** B)):
            temp = req.copy()

            count = 0
            for bits in (shops.keys()):
                mask = (i >> (bits - 1)) & 1
                count += 1
                for m in shops[bits]:
                    if temp.__contains__(m):
                        temp.remove(m)

            if not temp:
                ans = min(ans, count)


        if ans == sys.maxsize:
            print(-1)
        else:
            print(ans)


A = 6
B = 20
C = [
  [2, 10],
  [1, 14],
  [5, 13],
  [4, 9],
  [6, 1],
  [1, 3],
  [3, 8],
  [6, 11],
  [6, 16],
  [1, 5],
  [2, 7],
  [2, 2],
  [5, 18],
  [5, 12],
  [3, 4],
  [5, 19],
  [6, 20],
  [2, 15],
  [3, 17],
  [1, 6]
]


D = 3
E  = [
  [3, 19],
  [2, 19],
  [1, 19],
  [3, 16]
]

s=Solution()
s.solve(A,B,C,D,E)
