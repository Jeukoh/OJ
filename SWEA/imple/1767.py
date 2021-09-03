dx = [-1,0,1,0]
dy = [0,-1,0,1]

def checkcore(loc): # 가능한 방향을 반환
    x,y = loc
    if x == 0 or x == N-1 or y ==0 or y == N-1:
        return
    ret = (1<<4)-1
    for _ in range(4):
        nx, ny = x, y
        while N-1>nx>0 and N-1>ny>0:
            nx += dx[_]
            ny += dy[_]
            if Map[nx][ny] != 0:
                ret -= 1<<_
                break
    return ret

def make_line(loc,dir): # 가능한 방향으로 라인을 그림
    x,y = loc
    nx, ny = x+dx[dir], y+dy[dir]
    ret = 0
    while N > nx >= 0 and N > ny >= 0:
        Map[nx][ny] = 2
        ret += 1
        nx += dx[dir]
        ny += dy[dir]
    return ret
def del_line(loc,dir): # 라인을 지움
    x, y = loc
    nx, ny = x+dx[dir], y+dy[dir]
    while N > nx >= 0 and N > ny >= 0:
        Map[nx][ny] = 0
        nx += dx[dir]
        ny += dy[dir]

def dfs(k,anw,sel):
    global min_anw, max_select, NCo
    if max_select > sel+(NCo-k):
        return
    if k == NCo:
        if sel > max_select:
            max_select = sel
            min_anw = anw
        elif sel == max_select:
            min_anw = min(min_anw, anw)

        return
    log = core_map[k]
    ret = checkcore(log)
    for dir in range(4):
        if ret & 1<<dir:
            dfs(k+1,anw+make_line(log,dir),sel+1)
            del_line(log,dir)
    if max_select != NCo:
        dfs(k+1,anw,sel)

for tc in range(1,int(input())+1):
    N = int(input())
    Map = [list(map(int,input().split())) for _ in range(N)]
    core_map = []

    for i in range(1,N-1):
        for j in range(1,N-1):
            if Map[i][j] == 1:
                core_map.append((i,j))
    NCo = len(core_map)
    min_anw = 100000000
    max_select = 0
    dfs(0,0,0)
    print(f'#{tc}', min_anw)