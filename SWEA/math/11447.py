for tc in range(1, int(input()) + 1):
    N=int(input())
    num_list = list(map(int, input().split()))
    min_value = min(num_list)
    anw = 0
    num_dx = 500
    dx = min_value/num_dx
    dp = [[0]*(num_dx) for _ in range(N)]
    for idx in range(num_dx):
        x = dx*idx+(1e-16)
        height = 1
        for j in range(1,N):
            height *= (num_list[j]-x)/num_list[j]
        dp[0][idx] = height/num_list[0]

    for i in range(1,N):
        for idx in range(num_dx):
            x = dx*idx+(1e-16)
            dp[i][idx] = dp[i-1][idx]*((num_list[i-1]-x)/(num_list[i]-x))

    for i in range(N):
        #anw += (i+1)*((dp_greedy[i][0]/2+sum(dp_greedy[i][1:-1])+dp_greedy[i][-1]/2))*dx
        anw += (i+1)*(dp[i][0]+dp[i][-1]+4*sum(dp[i][1:-1:2])+2*sum(dp[i][2:-2:2]))*dx/3


    print("#{}".format(tc), "{:.8f}".format(anw))
