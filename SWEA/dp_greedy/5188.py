for tc in range(1,int(input())+1):
    N = int(input())

    dp = [list(map(int,input().split())) for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if x == 0 and y == 0:
                continue
            if x == 0:
                dp[x][y] += dp[x][y-1]
                continue
            if y == 0:
                dp[x][y] += dp[x-1][y]
                continue

            dp[x][y] += min(dp[x-1][y],dp[x][y-1])

    print(f'#{tc}', dp[-1][-1])