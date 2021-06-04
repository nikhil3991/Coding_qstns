def dnf(arr):
    n = len(arr)
    low = 0
    mid =0
    high = n-1
    while mid<=high:
        if arr[mid] == 'G':
            arr[low],arr[mid] = arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid] == 'R':
            mid+=1
        else:
            arr[mid],arr[high] = arr[high],arr[mid]
            high-=1
    print(arr)


arr = ['R','G','B','G','B','B','R','G','R']
dnf(arr)