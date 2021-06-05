class Solution:
    def largestComponentSize(self, A):
        n = len(A)

        def prime_factors(x):
            factors = set()
            while x % 2 == 0:
                factors.add(2)
                x = x // 2
            for i in range(3, int(x ** 0.5) + 1, 2):
                while x % i == 0:
                    factors.add(i)
                    x = x // i
            if x > 2:
                factors.add(x)
            return factors

        def find(x):
            while x != parents[x]:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x

        def union(x, y):
            x = find(x)
            y = find(y)
            if x == y:
                return
            parents[x] = y
            sizes[y] += sizes[x]
            sizes[x] = 0

        parents = [i for i in range(n)]
        sizes = [1] * n
        prime_to_index = {}
        for i, a in enumerate(A):
            primes = prime_factors(a)
            for p in primes:
                if p in prime_to_index:
                    union(i, prime_to_index[p])
                prime_to_index[p] = i
        return max(sizes)



S=Solution()
A = [2,3,6,7,4,12,21,39]
B=[20,50,9,63]
a= S.largestComponentSize(A)
b=S.largestComponentSize(B)
print(a,b)
