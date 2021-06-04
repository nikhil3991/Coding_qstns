def solve(A):
    if A <= 2:
        return A
    a = 1
    b = 2
    for i in range(3, A + 1):
        c = b + (i - 1) * a
        a = b
        b = c % (10003)
    print(c%10003)

for i in range(5):
    print(solve(i))
