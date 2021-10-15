from collections import deque

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs():
    S = deque([(0,0)])

    while S:
        x, y = S.popleft()
        for _ in range(4):
            nx, ny = x+dx[_], y+dy[_]
            if N>nx>=0 and N>ny>=0 and cost_Map[x][y]+Map[nx][ny] < cost_Map[nx][ny]:
                S.append((nx,ny))
                cost_Map[nx][ny] = cost_Map[x][y]+Map[nx][ny]



for tc in range(1,int(input())+1):
    N = int(input())
    Map = [list(map(int,input())) for _ in range(N)]

    cost_Map = [[9*N*N]*N for _ in range(N)]
    cost_Map[0][0] = 0

    bfs()
    print(f'#{tc} {cost_Map[-1][-1]}')