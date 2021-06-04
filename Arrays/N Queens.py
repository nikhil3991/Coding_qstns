def solveNQueens(A):
    # n=len(A)
    if A == 0 or A == 2 or A == 3:
        return []
    res = []
    queen_loc = [0] * A

    def utility(row):
        if row == A:
            temp=queen_loc.copy()
            res.append(temp)
            # queen_loc.clear()
            return
        for col in range(A):
            if isValid(col, queen_loc, row):
                queen_loc[row] = col
                # print(res)
                # print("-"*40)
                utility(row + 1)

    def isValid(col_index, queen_loc, row_index):
        for row in range(row_index):
            if queen_loc[row] == col_index:
                return False
            temp = row_index - row
            column_diff = abs(queen_loc[row] - col_index)
            if column_diff == temp:
                return False
        return True

    utility(0)
    print(res)

solveNQueens(4)