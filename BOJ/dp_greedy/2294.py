import sys; readline = sys.stdin.readline
import math
#from pprint import pprint

N, K = map(int,readline().split())
coin = []
for _ in range(N):
    coin.append(int(readline()))

dp = [[math.inf]*(K+1) for _ in range(N+1)]


for i,v in enumerate(coin):
    if v <= K:
        dp[0][v] = 1


for n in range(1,N+1):
    for k in range(1,K+1):
        if k >= coin[n-1]:
            dp[n][k] = min(dp[n-1][k],dp[n][k-coin[n-1]]+1)
        else:
            dp[n][k] = dp[n-1][k]

        #pprint(dp_greedy)

if dp[-1][-1] == math.inf:
    print(-1)
else:
    print(dp[-1][-1])
