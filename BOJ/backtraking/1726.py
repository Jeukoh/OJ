dx = [-1,0,1,0] # 북 서 남 동
dy = [0,-1,0,1]

dir_dict = {0:3,1:1,2:2,3:0}

import sys; readline = sys.stdin.readline

def bfs(sx,sy,sd):
    visited = [[[True]*4 for _ in range(M)] for _ in range(N)]
    visited[sx][sy][sd] = False
    Q = [[sx,sy,sd]]
    cnt = 0
    if not visited[fx][fy][fd]:
        return cnt
    while Q:
        #print(cnt,Q)
        tmp_Q = []
        cnt += 1
        for x,y,d in Q:
            nx,ny,nd = x,y,d
            for _ in range(3):
                nx += dx[d]
                ny += dy[d]
                if not (N>nx>=0 and M>ny>=0 and not Map[nx][ny]):
                    break
                if visited[nx][ny][nd]:
                    tmp_Q.append([nx,ny,nd])
                    visited[nx][ny][nd] = False

            nx,ny,nd = x,y,d
            for _ in range(1,4,2):
                nd = (d+_)%4
                if visited[nx][ny][nd]:
                    tmp_Q.append([nx,ny,nd])
                    visited[nx][ny][nd] = False
            if not visited[fx][fy][fd]:
                return cnt

        Q = tmp_Q[:]



N, M = map(int,readline().split())
Map = [list(map(int,readline().split())) for _ in range(N)]
sx,sy,sd = map(lambda x: int(x)-1,readline().split())
fx,fy,fd = map(lambda x: int(x)-1,readline().split())
sd = dir_dict[sd]
fd = dir_dict[fd]
print(bfs(sx,sy,sd))