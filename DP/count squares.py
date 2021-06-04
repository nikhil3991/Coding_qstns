# def countSquares(matrix):
#     m = len(matrix)
#     n = len(matrix[0])
#     count = 0
#     for i in range(1,m):
#         for j in range(1,n):
#             if matrix[i][j] == 0:
#                 continue
#             x = min(matrix[i - 1][j], matrix[i - 1][j - 1], matrix[i][j - 1])
#             matrix[i][j] = 1 + x
#             count+=matrix[i][j]
#     print(count)
#     for i in range(m):
#         print(matrix[i])
#
# A=[
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# countSquares(A)

def find():
    print("10")
    return True

find()