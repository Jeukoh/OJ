def dfs(i,anw):
    global min_anw
    if i == N:
        if min_anw > anw:
            min_anw = anw
        return

    if anw > min_anw:
        return

    for idx in range(N):
        if row[idx]:
            row[idx] = False
            dfs(i+1,anw+Map[i][idx])
            row[idx] = True


for tc in range(1,int(input())+1):
    N = int(input())
    Map = [list(map(int,input().split())) for _ in range(N)]
    row = [True]*N


    min_anw = N*10+1
    dfs(0,0)
    print(f'#{tc} {min_anw}')