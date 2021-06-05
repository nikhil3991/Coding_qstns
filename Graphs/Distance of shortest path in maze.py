class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer

    def solve(self, A, B, C):

        m = len(A)
        n = len(A[0])
        q = []
        visited = set()

        def vertical(t):
            return t in {'d', 'u'}

        def perpendicular(t):
            if vertical(t):
                return ["r", "l"]
            else:
                return ["u", "d"]

        count = 0
        dirns = {"d": (1, 0), "u": (-1, 0), "r": (0, 1), "l": (0, -1)}
        for i in dirns.keys():
            q.append((B[0], B[1], i))
        while q:
            new_queue = []
            while q:
                x, y, dir = q.pop()
                if (x, y, dir) in visited:
                    continue
                visited.add((x, y, dir))
                nx, ny = dirns[dir]
                if 0 <= x + nx < m and 0 <= y + ny < n and A[x + nx][y + ny] == 0:
                    new_queue.append((x + nx, y + ny, dir))
                else:
                    if [x, y] == C:
                        print(count)
                        return
                    temp = perpendicular(dir)
                    for i in temp:
                        q.append((x, y, i))
            count += 1
            q = new_queue

        print(-1)
A = [
  [1, 1, 0, 1],
  [0, 0, 0, 1],
  [1, 0, 0, 1],
  [0, 0, 1, 0]
]
B = [ 1, 1 ]
C = [ 2, 1 ]
s=Solution()
s.solve(A,B,C)
