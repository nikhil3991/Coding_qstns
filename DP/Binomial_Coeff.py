

def solve(n,c):
    def utility(x,y):
        if y == 0 or y == x:
            return 1
        if temp[x][y]==0:
            without_y = utility(x-1,y)
            with_y = utility(x-1,y-1)
            temp[x][y] = with_y + without_y
        return temp[x][y]
    temp = [[0]*(c+1) for i in range(n+1)]
    print(utility(n,c))
    for i in temp:
        print(i,end = "\n")


n=8
c=4
solve(n,c)