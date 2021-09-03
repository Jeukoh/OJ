import sys; readline = sys.stdin.readline

N, M = map(int,readline().split())

n_list = sorted([0]+list(map(int,readline().split())))
m_list = sorted([0]+list(map(int,readline().split())))

if M > N:
    n_list, m_list = m_list, n_list
    N, M = M, N

dp = [[0]*(M+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        if j <= i:
            if i == j:
                dp[i][j] = dp[i-1][j-1]+abs(n_list[i]-m_list[j])
            else:
                dp[i][j] = min(dp[i-1][j-1]+abs(n_list[i]-m_list[j]),dp[i-1][j])

            #print(i,j)
            #print(*dp_greedy,sep='\n')

print(dp[-1][-1])
