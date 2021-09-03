def maxv(arr):
    if len(arr)%2:
        arr += [0]
    dp = [[0]*2 for _ in range(len(arr)//2+2)]
    for idx in range(2,len(arr)//2+2):
        dp[idx][0] = arr[(idx-2)*2]+ max(dp[idx-2][1],dp[idx-1][0])
        dp[idx][1] = arr[(idx-2)*2+1] + max(dp[idx-1][1],dp[idx-1][0])

    return max(dp[-1])

for tc in range(1,int(input())+1):
    N, M = map(int,input().split())
    anw = [0]*N
    for _ in range(N):
        anw[_] = maxv(list(map(int, input().split())))
    print(f'#{tc} {maxv(anw)}')