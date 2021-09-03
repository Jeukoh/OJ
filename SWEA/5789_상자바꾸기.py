T = int(input())
for t in range(1,T+1):
    N, Q = map(int, input().split())
    LR_list = []
    anw = [0]*(N+1)
    for _ in range(Q):
        LR_list.append(list(map(int, input().split())))
    for idx in range(Q-1,-1,-1):
        L, R = LR_list[idx]
        for i in range(L,R+1):
            if anw[i]:
                continue
            else:
                anw[i] = idx+1

    print(f'#{t} {" ".join(str(x) for x in anw[1:])}')