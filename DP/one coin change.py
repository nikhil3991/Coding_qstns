# Recursion
def totalways(arr,n,key):
    if key == 0:
        return 1
    if key <0:
        return 0
    if n<=0 and key >0:
        return 0
    return totalways(arr,n-1,key)+totalways(arr,n,key-arr[n-1])



# Dynamic Programming
def count(arr,m,key):
    table = [0 for k in range(key+1)]
    table[0]=1
    print(table)
    for i in range(0,m):
        for j in range(arr[i],key+1):
            table[j]+=table[j-arr[i]]
        print(table)
    # print(table)

    return table[key]

arr = [1,3,4]
res= totalways(arr,len(arr),17)
print(res)
print("----"*16)
print(count(arr,len(arr),5))