def countDecodingDP(digits):
    n=len(digits)
    count = [0] * (n + 1) # A table to store
    # results of subproblems
    count[0] = 1
    count[1] = 1

    for i in range(2, n + 1):

        count[i] = 0

        # If the last digit is not 0, then last
        # digit must add to the number of words
        if (digits[i - 1] > '0'):
            count[i] = count[i - 1]

        # If second last digit is smaller than 2
        # and last digit is smaller than 7, then
        # last two digits form a valid character
        if (digits[i - 2] == '1' or
                (digits[i - 2] == '2' and
                 digits[i - 1] < '7')):
            count[i] += count[i - 2]

    return count[n]
num="1234"
print(countDecodingDP(num))
