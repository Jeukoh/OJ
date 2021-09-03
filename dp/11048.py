import sys; readline = sys.stdin.readline

X,Y  = map(int,readline().split())
Map = []
for _ in range(X):
    Map.append(list(map(int,readline().split())))
dp = [[0]*(Y+1) for _ in range(X+1)]
for x in range(1,X+1):
    for y in range(1,Y+1):
        dp[x][y] = Map[x-1][y-1]+max(dp[x-1][y],dp[x-1][y-1],dp[x][y-1])

print(dp[-1][-1])