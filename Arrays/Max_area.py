def maxArea(self, h: int, w: int, horizontalCuts, verticalCuts) -> int:
    m = len(horizontalCuts)
    n = len(verticalCuts)
    horizontalCuts.sort()
    verticalCuts.sort()
    if m == 1 and n == 1:
        a = max(horizontalCuts[0], h - horizontalCuts[0])
        b = max(verticalCuts[0], w - verticalCuts[0])
        return a * b

    m1 = 1
    m2 = 1
    for i in range(1, m):
        m1 = max(m1, horizontalCuts[i] - horizontalCuts[i - 1])
    for i in range(1, n):
        m2 = max(m2, verticalCuts[i] - verticalCuts[i - 1])
    if m == 1 or n == 1:
        if n == 1:
            return m1 * (max(verticalCuts[0], w - verticalCuts[0]))
        else:
            m2 * (max(horizontalCuts[0], h - horizontalCuts[0]))
    return m1 * m2