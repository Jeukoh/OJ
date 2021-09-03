T = int(input())

for t in range(1,T+1):
    N, K = map(int,input().split())
    N_list = list(map(int,input().split()))

    cnt = 0
    for i in range(1<<N): # 부분집합 경우의 수
        partial_sum = 0
        for j in range(N): # idx
            if i & (1<<j):
                partial_sum += N_list[j]

        if partial_sum == K:
            cnt += 1

    print(f'#{t} {cnt}')