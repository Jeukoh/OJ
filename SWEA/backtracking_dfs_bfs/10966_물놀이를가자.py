from collections import deque
dx = [-1,0,1,0]
dy = [0,-1,0,1]
def bfs(Ss:list):
    Q = deque([S for S in Ss])
    while Q:
        x,y = Q.popleft()
        for _ in range(4):
            nx, ny = x+dx[_], y+dy[_]
            if R>nx>=0 and C>ny>=0 and Map[nx][ny] == 'L' and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                Q.append([nx,ny])


for tc in range(1,int(input())+1):
    R, C = map(int,input().split())
    Map = [input() for _ in range(R)]
    visited = [[0]*C for _ in range(R)]
    Ss = []
    for x in range(R):
        for y in range(C):
            if Map[x][y] == 'W':
                Ss.append((x,y))
    bfs(Ss)
    anw = 0
    for r in range(R):
        anw += sum(visited[r])
    print(f'#{tc}', anw)