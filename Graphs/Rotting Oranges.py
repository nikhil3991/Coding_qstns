def solve(A):
    n = len(A[0])
    m = len(A)
    fresh = set()
    rotten = set()
    for i in range(m):
        for j in range(n):
            if A[i][j] == 1:
                fresh.add((i, j))
            if A[i][j] == 2:
                rotten.add((i, j))
    time = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while fresh:
        time += 1
        new_rotten = set()
        for (x, y) in rotten:
            for i in range(4):
                if (x + dx[i], y + dy[i]) in fresh:
                    new_rotten.add((x + dx[i], y + dy[i]))
                    # fresh.remove((x + dx[i], y + dy[i]))
        print(new_rotten)
        if not new_rotten:
            print(-1)
            return
        rotten = new_rotten
        fresh -= new_rotten
    print(time)

A=[
  [2, 0, 2, 2, 2, 0, 2, 1, 1, 0],
  [0, 1, 2, 0, 2, 0, 0, 1, 0, 1],
  [0, 1, 1, 1, 2, 0, 1, 1, 2, 1],
  [2, 0, 2, 0, 1, 1, 2, 1, 0, 1],
  [1, 0, 1, 1, 0, 1, 2, 0, 2, 2],
  [0, 2, 1, 1, 2, 2, 0, 2, 1, 2],
  [2, 1, 0, 2, 0, 0, 0, 0, 1, 1],
  [2, 2, 0, 2, 2, 1, 1, 1, 2, 2],
]
solve(A)