for tc in range(1,int(input())+1):
    N = int(input())
    dock_time = list(list(map(int,input().split())) for _ in range(N))
    dock_time.sort(key=lambda x: x[1])
    anw = 0
    nt = 0
    for st, et in dock_time:
        if st >= nt:
            anw += 1
            nt = et

    print(f'#{tc}', anw)