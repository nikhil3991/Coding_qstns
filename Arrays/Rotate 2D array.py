# def rotate(A):
#     N = len(A[0])
#     for i in range(N // 2):
#         for j in range(i, N - i - 1):
#             temp = A[i][j]
#             A[i][j] = A[N - 1 - j][i]
#             A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
#             A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
#             A[j][N - 1 - i] = temp
#     print(arr)



def rotate(A):
    n = len(A[0])
    for layer in range(n//2):
        first = layer
        last = n-1-layer
        for i in range(first,last):
            offset = i-first
            top = A[first][i]
            A[first][i] = A[last-offset][first]
            A[last-offset][first] = A[last][last-offset]
            A[last][last-offset] = A[i][last]
            A[i][last] = top
    print(A)





def solve(A):
    n=len(A)
    for layer in range(n//2):
        first = layer
        last = n-1-layer
        for i in range(first,last):
            offset = i-first
            temp = A[first][i]
            A[first][i] = A[last-offset][first]
            A[last-offset][first] = A[last][last-offset]
            A[last][last-offset] = A[i][last]
            A[i][last] = temp
    print(A)


arr = [[1,2,3],[5,6,7],[8,9,10]]
print(len(arr))
rotate(arr)
solve(arr)


