
def atMostsum(arr,n,k):
    count=0
    sum =0
    max_cnt =0
    for i in range(n):
        if sum+arr[i]<k:
            sum+=arr[i]
            count+=1
        elif k!=0:
            sum = sum - arr[i - count] + arr[i]

        max_cnt = max(count,max_cnt)
    return max_cnt


arr = [1,2,1,0,1,1,0]
n=len(arr)
k=4
print(atMostsum(arr,n,k))