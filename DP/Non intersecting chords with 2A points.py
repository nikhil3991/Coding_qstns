def chordCnt(A):
    if A <= 2:
        return A
    ways = [0] * (A + 1)
    for i in range(3):
        ways[i] = i
    ways[0] = 1
    for i in range(3, A + 1):
        n = i // 2
        for j in range(n):
            ways[i] += 2 * (ways[j] * ways[i - j - 1])
        if i % 2 == 1:
            ways[i] += ways[n] * ways[n]
    print(ways)
    print(ways[A] % (10 ** 9 + 7))

A=13
chordCnt(A)