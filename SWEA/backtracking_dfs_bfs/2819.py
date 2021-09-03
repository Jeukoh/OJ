dx = (-1,0,1,0)
dy = (0,-1,0,1)

def bfs():
    global anw_set
    while stack:
        x,y,anw = stack.pop()
        if len(anw) == 7:
            anw_set.add(anw)
            continue
        for _ in range(4):
            nx,ny = x+dx[_], y+dy[_]
            if 4>nx>=0 and 4>ny>=0:
                stack.append([nx,ny,anw+Map[nx][ny]])




    pass

for tc in range(1,int(input())+1):
    N = 4
    Map = [input().split() for i in range(N)]
    anw_set = set()
    stack = [[i,j,Map[i][j]] for i in range(N) for j in range(N)]

    bfs()
    print(f'#{tc} {len(anw_set)}')


