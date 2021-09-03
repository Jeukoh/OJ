T = 10

for _ in range(1,T+1):

    K = int(input())

    height = list(map(int,input().split()))

    count_height = [0]*101


    for i in height:
        count_height[i] += 1


    acum_height = [0]*101
    acum_height2 = [0]*101
    acum_height[-1] = count_height[-1]
    acum_height2[0] = count_height[0]
    for idx in range(99,-1,-1):
        acum_height[idx] = acum_height[idx+1]+count_height[idx]
        acum_height2[100-idx] = acum_height2[100-idx-1]+count_height[100-idx]


    cnt1 = 0
    cnt2 = 0
    for idx in range(1,101):
        cnt2 += acum_height2[idx]
        if cnt2 > K:
            min_height = idx
            break

    for idx in range(100,0,-1):
        cnt1 += acum_height[idx]
        if cnt1 > K:
            max_height = idx
            break

    anw = max_height-min_height
    if anw < 0:
        anw = 1 if acum_height2[-1] % 2 else 0

    print(f'#{_} {anw}')