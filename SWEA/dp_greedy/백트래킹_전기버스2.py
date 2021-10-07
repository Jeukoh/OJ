# for tc in range(1,int(input())+1):
#     tmp = list(map(int,input().split()))
#     N = tmp[0]; arr = tmp[1:]+[0]
#     cnt = 0
#     while N>1:
#         cur = 0
#         while arr[cur]+cur < N-1:
#             cur += 1
#         cnt += 1
#         arr = arr[:cur+1]
#         N = cur+1
#     print(f'#{tc}', cnt-1)


# ----- 다른 풀이

for tc in range(1,int(input())+1):
    tmp = list(map(int,input().split()))
    N = tmp[0]; arr = tmp[1:]+[0]
    dp = [0]*N
    num = 1
    for idx, v in enumerate(arr):
        for j in range(min(N-1,v+idx),idx-1,-1):
            if dp[j]:
                break
            dp[j] = dp[idx] + 1
        if dp[-1]:
            break

    print(f'#{tc}',dp[-1]-1)