from collections import deque
dx = (-1,0,1,0,-1,-1,1,1)
dy = (0,-1,0,1,-1,1,-1,1)

def bfs(x,y):
    stack = deque([(x,y)])
    while stack:
        x,y = stack.popleft()
        for _ in range(8):
            nx, ny = x + dx[_], y + dy[_]
            if N > nx >= 0 and N > ny >= 0 and tb[nx][ny] >= 0 and visited[nx][ny]:
                visited[nx][ny] = False
                if tb[nx][ny] == 0:
                    stack.append((nx,ny))

    return 1

for tc in range(1,int(input())+1):
    N = int(input())
    star = []
    zero = []
    tb = []
    visited = [[True]*N for _ in range(N)]
    for i in range(N):
        tmp=list(map(lambda x: 0 if x == '.' else -1, list(input())))
        tb.append(tmp)
        for j in range(N):
            if tmp[j] == -1:
                star.append((i,j))

    for x,y in star:
        visited[x][y] = False
        for _ in range(8):
            nx, ny = x+dx[_], y+dy[_]
            if N>nx>=0 and N>ny>=0 and tb[nx][ny] >= 0:
                tb[nx][ny] += 1

    tmp = []
    anw = 0
    for x in range(N):
        for y in range(N):
            if visited[x][y] and tb[x][y] == 0:
                visited[x][y] = False
                anw += bfs(x,y)
            elif visited[x][y]:
                tmp.append((x,y))

    for x,y in tmp:
        if visited[x][y]:
            anw += 1
    print(f'#{tc} {anw}')