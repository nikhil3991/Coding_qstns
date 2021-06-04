from collections import defaultdict
def solve(A):
    n = len(A)
    print(A)
    count = 0
    sequences = []
    for i in range(n):
        sequences.append(defaultdict(int))
        for j in range(i):
            diff = A[i]-A[j]
            diff_count   = sequences[j].get(diff,0)
            count+=diff_count
            sequences[-1][diff]+= diff_count+1

        for k in sequences:
            print(k,end= " ")
        print()
        print(count)



    print(count)


A = [1, 3, 5, 7, 9]

solve(A)