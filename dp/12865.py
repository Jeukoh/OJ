import sys; readline = sys.stdin.readline
from pprint import pprint
N, K = map(int,readline().split())
value = []
weight = []
for _ in range(N):
    x,y = map(int,readline().split())
    weight.append(x)
    value.append(y)

weight.insert(0,0)
value.insert(0,0)
print(f'weight {weight}')
print(f'value {value}')

dp = [[0]*(K+1) for _ in range(N+1)] # dp_greedy[N][K]
#dp_greedy[N][K]
#N번째까지 넣었고, 최대 무게가 K일떄 최대 벨류
for i in range(1,N+1):
    for j in range(1,K+1):
        if weight[i] <= j:
            dp[i][j] = max(dp[i-1][j-weight[i]]+value[i],dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

        print(f' i,j {i,j}')
        pprint(dp)


print(dp[-1][-1])




