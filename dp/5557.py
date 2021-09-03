import sys; readline = sys.stdin.readline
from pprint import pprint

N = int(input())
numl = list(map(int,input().split()))
dp = [[0]*21 for _ in range(N-1)]
dp[0][numl[0]] = 1
for idx,v in enumerate(numl[:-1]):
    if idx == 0:
        continue
    for j in range(21):
        if j-v >= 0 and dp[idx-1][j-v]: dp[idx][j] += dp[idx-1][j-v]
        if j+v <= 20 and dp[idx-1][j+v]: dp[idx][j] += dp[idx-1][j+v]
pprint(dp[-1][numl[-1]])