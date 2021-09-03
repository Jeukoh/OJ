for tc in range(1,11):
    N = int(input())
    Map = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    #flag = True # 1 접촉안댐
    # flag = False # 1 접촉 된 상태
    for j in range(N):
        flag = True
        for i in range(N):
            if flag and Map[i][j] == 1:
                flag = False
            elif not flag and Map[i][j] == 2:
                cnt += 1
                flag = True

    print(f'#{tc}',cnt)