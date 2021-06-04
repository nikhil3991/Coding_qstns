def solve(A):
    n = len(A)
    if n == 1:
        return 1
    A.sort(key=lambda m: m[0] and m[1], reverse=True)
    A.sort(key=lambda m: m[0])
    temp = []
    for i in range(n):
        if temp and A[i][1] <= temp[-1]:
            for j in range(len(temp)):
                if temp[j] < A[i][1]:
                    pass
                else:
                    temp[j] = A[i][1]
                    break
        else:
            temp.append(A[i][1])
    print(len(temp))

A = [
  [11, 10],
  [14, 6],
  [7, 18],
  [6, 7],
  [11, 4],
  [13, 19],
  [3, 8],
  [16, 15],
  [18, 15]
]
solve(A)



