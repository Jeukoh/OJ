dx = [-1,0,1,0]
dy = [0,-1,0,1]

from collections import deque
from pprint import pprint

# Map[nx][ny]로 입장할 때 가능한 방향들만
pass_dict = {1:[0,1,2,3],2:[0,2],3:[1,3],4:[1,2],5:[0,1],6:[0,3],7:[2,3]}

def genedir(x,y):
    if Map[x][y] == 1:
        yield from [0,1,2,3]
    if Map[x][y] == 2:
        yield from [0,2]
    if Map[x][y] == 3:
        yield from [1,3]
    if Map[x][y] == 4:
        yield from [0,3]
    if Map[x][y] == 5:
        yield from [2,3]
    if Map[x][y] == 6:
        yield from [1,2]
    if Map[x][y] == 7:
        yield from [0,1]


def bfs(R,C,L):

    visited = [[0]*M for _ in range(N)]
    Q = deque([[R,C]])
    visited[R][C] = 1
    cnt = 0
    while Q:
        x,y = Q.popleft()
        cnt += 1
        for _ in genedir(x,y):
            #print(x,y,_,Map[x][y])
            nx, ny = x+dx[_], y+dy[_]
            if N>nx>=0 and M>ny>=0 and not visited[nx][ny] and Map[nx][ny] != 0 and _ in pass_dict[Map[nx][ny]]:
                visited[nx][ny] = visited[x][y] + 1
                if visited[nx][ny] <= L:
                    Q.append([nx,ny])
            #print(Q)
    #pprint(visited)

    return cnt

for tc in range(1,int(input())+1):
    N,M,R,C,L = map(int,input().split())

    Map = [list(map(int,input().split())) for _ in range(N)]

    #pprint(Map)
    anw = bfs(R,C,L)
    print(f'#{tc}', anw)