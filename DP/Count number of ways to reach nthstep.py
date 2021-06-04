# Recursive solution
def count(a):
    if a<0:
        return 0
    if a==0 or a==1:
        return 1
    if a==2:
        return 2
    else:
        return count(a-1)+count(a-2)+count(a-3)

#******************** O(logn) solution *********************
# class Solution {
# public int climbStairs(int n) {
# int[][] q = {{1, 1}, {1, 0}};
# int[][] res = pow(q, n);
#
#
# return res[0][0];
# }
# public
# int[][]
# pow(int[][]
# a, int
# n) {
# int[][]
# ret = {{1, 0}, {0, 1}};
# while (n > 0) {
# if ((n & 1) == 1) {
# ret = multiply(ret, a);
# }
# n >>= 1;
# a = multiply(a, a);
# }
# return ret;
# }
# public
# int[][]
# multiply(int[][]
# a, int[][]
# b) {
# int[][]
# c = new
# int[2][2];
# for (int i = 0; i < 2; i++) {
# for (int j = 0; j < 2; j++) {
# c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j];
# }
# }
# return c;
#
# }
# }


#     Dynamic Programming

def count1(a):
    if a<0:return 0
    if a<=1:return 1

    table = [0]*(a+1)
    table [0]=1
    table[1]=1
    table[2]=2
    for i in range(3,a+1):
        table[i]= table[i-1]+table[i-2]+table[i-3]
    return table[a]



n = 6
print(count(n))
print(count1(n))