import sys; readline = sys.stdin.readline

LN = int(readline())

def sol(N):
    dp = [[0]*(N+1) for _ in range(2)]
    #dp_greedy[k][N] k번쨰껄 집었을떄 최대값


    for i in range(1,N+1):
        for k in range(2):
            if i >= 2:
                dp[k][i] = max(dp[1-k][i-1]+sticker[k][i],dp[1-k][i-2]+sticker[k][i])
            else:
                dp[k][i] = dp[1-k][i-1]+sticker[k][i]

    anw = max(dp[0][-1],dp[1][-1])
    return anw

for _ in range(LN):
    N = int(readline())
    sticker = list()
    for __ in range(2):
        sticker.append(list(map(int,[0]+readline().split())))

    print(sol(N))
