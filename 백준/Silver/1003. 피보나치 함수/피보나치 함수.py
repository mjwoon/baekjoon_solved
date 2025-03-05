import sys

input = sys.stdin.readline

t = int(input())

dp = [0] * 41
zero = [0] * 41
one = [0] * 41

zero[0] = 1
one[1] = 1
zero[2] = 1
one[2] = 1

dp[1] = 1
dp[2] = 1

for i in range(t):
    x = int(input())
    for i in range(3, x + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        zero[i] = zero[i - 1] + zero[i - 2]
        one[i] = one[i - 1] + one[i - 2]
        
    print(zero[x], one[x])
