for tc in range(1,int(input())+1):
    N, K = map(int,input().split())
    Map = [list(map(int,input().split())) for _ in range(N)]


    anw = 0
    for i in range(N):
        row_cnt = 0
        col_cnt = 0
        for j in range(N):
            if Map[i][j]:
                row_cnt += 1
            else:
                if row_cnt == K:
                    anw += 1
                row_cnt = 0
            if Map[j][i]:
                col_cnt += 1
            else:
                if col_cnt == K:
                    anw += 1
                col_cnt = 0
        if row_cnt == K:
            anw += 1
        if col_cnt == K:
            anw += 1

    print(f'#{tc} {anw}')

