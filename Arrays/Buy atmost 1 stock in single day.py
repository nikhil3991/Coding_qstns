def findProfit(arr):
    n = len(arr)
    profit = 0
    maximum = 0
    for i in range(n-1,-1,-1):
        if arr[i] > maximum:
            maximum = arr[i]
        profit+=maximum - arr[i]
    return profit


arr = [1,2,5,4,21]
print(findProfit(arr))
