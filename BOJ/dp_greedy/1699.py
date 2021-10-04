import sys; readline = sys.stdin.readline
import math
N = int(readline())
dp = [i for i in range(N+1)]

for i in range(1,N+1):
    tmp = math.sqrt(i)

    if tmp.is_integer():
        dp[i] = 1
    else:
        anw_cand = []
        for j in range(1,int(tmp)+1):
            anw_cand.append(dp[i-j*j])

        dp[i] = min(anw_cand)+1



print(dp[-1])