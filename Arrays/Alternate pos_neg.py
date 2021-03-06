def rightRotate(arr, n, outOfPlace, cur):
    temp = arr[cur]
    for i in range(cur, outOfPlace, -1):
        arr[i] = arr[i - 1]
    arr[outOfPlace] = temp
    return arr


def rearrange(arr, n):
    outOfPlace = -1
    for index in range(n):
        if (outOfPlace >= 0):

            # if element at outOfPlace place in
            # negative and if element at index
            # is positive we can rotate the
            # array to right or if element
            # at outOfPlace place in positive and
            # if element at index is negative we
            # can rotate the array to right
            if ((arr[index] >= 0 and arr[outOfPlace] < 0) or
                    (arr[index] < 0 and arr[outOfPlace] >= 0)):
                arr = rightRotate(arr, n, outOfPlace, index)
                if (index - outOfPlace > 2):
                    outOfPlace += 2
                else:
                    outOfPlace = - 1

        if (outOfPlace == -1):

            # conditions for A[index] to
            # be in out of place
            if ((arr[index] >= 0 and index % 2 == 0) or
                    (arr[index] < 0 and index % 2 == 1)):
                outOfPlace = index
    return arr


A = [-1, -2, -3, 4, 5]
print(rearrange(A,len(A)))
