N = int(input())
dp = [[1]*10 for i in range(N)]
for i in range(1,N):
    for idx in range(0,10):
        dp[i][idx] = sum(dp[i-1][:idx+1])%10007

print(sum(dp[-1])%10007)