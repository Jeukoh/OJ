from collections import deque

dx = (-1,0,1,0)
dy = (0,-1,0,1)

def bfs(x,y):

    visited[x][y] = 1
    Q = deque([(x,y)])

    while Q:
        x, y = Q.popleft()
        for _ in range(4):
            nx,ny = x+dx[_], y+dy[_]
            if 0 <= nx < N and 0 <= ny < N and Map[nx][ny] == Map[x][y] - 1:
                visited[nx][ny] = visited[x][y] + 1
                Q.append((nx,ny))

for tc in range(1,int(input())+1):
    N = int(input())
    Map = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    anw = 0
    max_m = 0
    for x in range(N):
        for y in range(N):
            if not visited[x][y]:
                bfs(x,y)

    for x in range(N):
        for y in range(N):
            if visited[x][y] > max_m:
                max_m = visited[x][y]
                anw = Map[x][y]
            elif visited[x][y] == max_m and Map[x][y] < anw:
                anw = Map[x][y]



    print(f'#{tc}', anw, max_m)