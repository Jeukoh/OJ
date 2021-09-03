import sys; readline = sys.stdin.readline
N, K = map(int,input().split())
oJ = list(map(int,input().split()))
J = [oJ[0]]
for idx in range(1,N):
    if J[-1] == oJ[idx]:
        continue
    J.append(oJ[idx])
N = len(J)
# dp[i][j] i부터 j까지 할때 클릭의 최소 횟수.
# dp[i][j] = dp[i][k] + dp[k+1][j] + 1 의 최소 값
# i~k 랑 k+1
dp = [[sys.maxsize]*N for _ in range(N)]
for i in range(N):
    dp[i][i] = 0
#구간
for t in range(0,N):
    #시작
    for i in range(N-t):
        # j
        j = i+t
        # i~j 사이는 i+1,i+2,...j-1까지
        for _ in range(i,j):
            if J[i] == J[_+1]:
                dp[i][j] = min(dp[i][j],dp[i][_]+dp[_+1][j])
            else:
                dp[i][j] = min(dp[i][j], dp[i][_] + dp[_ + 1][j]+1)
print(dp[0][N-1])