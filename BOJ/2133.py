import sys; readline = sys.stdin.readline

N = int(readline())


dp = [0]*(N+1)
dp[0] = 1
dp[2] = 3

for i in range(3,N+1):
    if i%2 == 0:
        for j in range(i//2):
            dp[i] += dp[i-2*j]*2
        dp[i] += i//2


print(dp)




