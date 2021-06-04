def letterCombinations(A):
    def utility(A, index, prefix, ):
        if index == n:
            res.append(prefix)
            return
        value = int(A[index])
        temp = var[value]
        for i in temp:
            prefix += i
            utility(A, index + 1, prefix)
            prefix = prefix[:-1]

    res = []
    n = len(A)
    var = {0: ['0'], 1: ['1'], 2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'],
           6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']
           }
    utility(A, 0, "")
    print(res)
    # x="prudhvi"
    # n=len(res)
    # # print(res[584])
    # for i in range(n):
    #     if res[i]==x:
    #         print(i,res[i])
    #         return
    # print(False)



letterCombinations("726")