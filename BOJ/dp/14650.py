N = int(input())

dp = [0 for _ in range(N)]
# 0, 1, 2
if N == 1:
    print(0)
else:
    dp[0] = 0
    dp[1] = 2
    for i in range(2,N):
        dp[i] = 3*dp[i-1]

    print(dp[-1])