N, K = map(int,input().split())
const = 1000000000
# dp[n][k] -> k+1개 선택해서 합이 n인 경우의 수
# for r dp[n-r][0] + dp[r][k-1] =

dp = [[0]*K for _ in range(N+1)]
def find(n,k):
    if dp[n][k]:
        return dp[n][k]

    if k==0:
        dp[n][k] = 1
        return 1

    for i in range(n+1):
        dp[n][k] = (dp[n][k] + find(n-i,0)*find(i,k-1))%const


    return dp[n][k]


print(find(N,K-1))