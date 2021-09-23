for tc in range(1,int(input())+1):
    cost = list(map(int,input().split()))
    date = list(map(int,input().split()))
    dp = [0]+list(date[x]*cost[0] for x in range(12))
    for i in range(1,13):
        pass
        #1일권과 1달권 비교
        dp[i] = min(dp[i-1]+dp[i],dp[i-1]+cost[1])
        if i >= 3:
            dp[i] = min(dp[i],dp[i-3]+cost[2])


    dp[-1] = min(dp[-1],cost[-1])

    print(f'#{tc}',dp[-1])