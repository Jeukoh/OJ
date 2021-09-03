dx = [-1,0,1,0]
dy = [0,-1,0,1]

from pprint import pprint

def dfs(x,y,anw,chance):
    global max_anw
    if anw > max_anw:
        max_anw = anw

    now_h = Map[x][y]
    for _ in range(4):
        nx, ny = x+dx[_], y+dy[_]
        if Map[nx][ny] < now_h and visit[nx][ny]:
            visit[nx][ny] = False
            dfs(nx,ny,anw+1,chance)
            visit[nx][ny] = True
        elif Map[nx][ny]-K < now_h and chance and visit[nx][ny]:
            tmp=Map[nx][ny]
            Map[nx][ny] = now_h-1
            visit[nx][ny] = False
            dfs(nx,ny,anw+1,False)
            visit[nx][ny] = True
            Map[nx][ny] = tmp


for tc in range(1,int(input())+1):
    N, K = map(int,input().split())
    Map = [[21+K]*(N+2)]
    tmp_h = 0
    for i in range(N):
        tmp = list(map(int,input().split()))
        for j in range(N):
            if tmp[j] > tmp_h:
                h_stack = [(i+1,j+1)]
                tmp_h = tmp[j]
            elif tmp[j] == tmp_h:
                h_stack.append((i+1,j+1))
        Map.append([21+K]+tmp+[21+K])
    Map.append([21+K]*(N+2))

    max_anw = 0
    visit = [[True]*(N+2) for _ in range(N+2)]


    for i in h_stack:
        visit[i[0]][i[1]] = False
        dfs(i[0],i[1],1,True)
        visit[i[0]][i[1]] = True

    print(f'#{tc}',max_anw)