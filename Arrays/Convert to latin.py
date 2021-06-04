A="I speak Goat Latin"
A= list(A.split(" "))


def toGoatLatin(S):
    S = list(S.split(" "))
    n = len(S)
    vowels = ['A', 'a', 'I', 'i', 'E', 'e', 'O', 'o', 'U', 'u']
    res = []
    count = 1
    for word in S:
        if word[0] in vowels:
            temp = word + 'ma' + 'a' * count
            res.append(temp)
        else:
            if len(word) == 1:
                temp = word + 'ma' + 'a' * count
            else:
                x = word[0]
                temp = word[1:] + x + 'ma' + 'a' * count
            res.append(temp)
        res.append(" ")
        count += 1
    res.pop(-1)
    return "".join(i for i in res)


A="I speak Goat Latin"
ans = toGoatLatin(A)
print(ans)