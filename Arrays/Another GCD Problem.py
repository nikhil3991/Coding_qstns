class Solution:
    # @param A : list of integers
    # @return an integer
    def gcd(a, b):
        if b == 0:
            return a
        if a < b:
            a, b = b, a
        return self.gcd(a, b)

    def solve(self, A):
        n = len(A)
        ans = -9999999
        pfactors = {}
        pfactors[0] = set()
        pfactors[1] = set()
        pfactors[1].add(1)
        pfactors[0].add(0)
        temp = {}
        max_ele = 0
        for i in range(n):
            max_ele = max(max_ele, A[i])
        visited = [1] * (max_ele + 1)
        for i in range(2, max_ele + 1):
            if visited[i] == 1:
                for j in range(i, max_ele + 1, i):
                    if visited[j] == 1:
                        visited[j] = 0
                        temp[j] = i
                    try:
                        pfactors[j].add(i)
                    except:
                        pfactors[j]=set()
                        pfactors[j].add(i)
        # for i in range(n):
        #     x = A[i]
        #     y = temp[A[i]]
        #     pfactors[A[i]] = set()
        #     pfactors[A[i]].add(y)
        #
        #     while x > 1:
        #         while x > 1 and x % y == 0:
        #             x = x // y
        #         if x <= 1:
        #             pass
        #         else:
        #             y = temp[x]
        #             pfactors[A[i]].add(y)

        print(A)
        print()
        print(pfactors)
        left = 0
        right = 1
        ans = 1
        # while right < n:
        #     flag = False
        #     for i in pfactors[A[left]]:
        #         if i in pfactors[A[right]]:
        #             flag = True
        #             break
        #     if flag:
        #         ans = max(ans, (right - left + 1))
        #         print(ans,left,right)
        #         right += 1
        #     else:
        #         left += 1
        while right<n:
            index = left-1
            for i in range(right,left-1,-1):
                flag = False
                for j in pfactors[A[i]]:
                    if j in pfactors[A[right]]:
                        flag = True
                        break
                if flag:
                    pass
                else:
                    index=i
                    break
            ans = max(ans,right-index)
            if index == left-1:
                right+=1
            else:
                left = index + 1



        print(ans)

s= Solution()
A= [ 4, 6, 25, 2, 25, 9, 25, 6, 9, 4, 12, 6, 6 ]
B= [6, 9, 4]
C= [ 4, 9, 6, 8, 25, 2, 6, 6, 4, 5, 3 ]
s.solve(C)
# s.solve(B)









