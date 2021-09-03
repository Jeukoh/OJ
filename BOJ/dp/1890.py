import sys; readline = sys.stdin.readline
from pprint import pprint
N = int(input())
Map = []

for _ in range(N):
    Map.append(list(map(int,readline().split())))

dp = [[0]*(N) for _ in range(N)]
dp[0][0] = 1

for x in range(N):
    for y in range(N):
        if x == N-1 and y == N-1:
            break
        if dp[x][y] >= 1:
            if y+Map[x][y] < N:
                dp[x][y+Map[x][y]] += dp[x][y]
            if x+Map[x][y] < N:
                dp[x+Map[x][y]][y] += dp[x][y]

print(dp[-1][-1])
