from pprint import pprint
T = int(input())
for t in range(1,1+T):
    N = int(input())
    N_list = list(map(int,input().split()))

    #dp_greedy[N][21]
    dp= [[0]*(21) for _ in range(N-1)]

    dp[0][N_list[0]] = 1

    C = 1234567891

    for i in range(1,N-1):
        for j in range(21):
            if j + N_list[i] <= 20:
                dp[i][j] = (dp[i][j]+dp[i-1][j+N_list[i]])%C
            if j - N_list[i] >= 0:
                dp[i][j] = (dp[i][j]+dp[i-1][j-N_list[i]])%C

    print(f'#{t} {dp[-1][N_list[-1]]}')