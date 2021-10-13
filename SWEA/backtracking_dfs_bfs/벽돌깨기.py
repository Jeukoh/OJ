from collections import deque
from pprint import pprint

dx = (-1,0,1,0)
dy = (0,-1,0,1)

# 1. 벽돌 뿌시는거 구현
# x 좌표에 map
# return -> 부신 벽돌 개수 + 바뀐 Map
def droptheball(x,Map):
    Map = Mapcopy(Map)
    y = 0
    while y < H and not Map[x][y]:
        y += 1
    if y == H:
        return 0, Map
    # x,y를 시작으로 연쇄적으로 -> bfs
    ret = 1
    Q = deque([[x,y,Map[x][y]]])
    Map[x][y] = 0
    while Q:
        x,y,k = Q.popleft()
        for _ in range(4):
            for v in range(1,k):
                ny, nx = y+v*dy[_], x+v*dx[_]
                # 다음 연쇄
                if 0 <= ny < H and 0 <= nx < W and Map[nx][ny]:
                    Q.append([nx,ny,Map[nx][ny]])
                    Map[nx][ny] = 0
                    ret += 1
    # 우로 정렬
    for w in range(W):
        if any(Map[w]):
            for h in range(H-1):
                if Map[w][h] and not Map[w][h+1]:
                    Map[w][:h+2] = [0]+Map[w][:h+1]
    return ret, Map

def dfs(i,Map,count):
    global Mincount
    if i == N:
        if count < Mincount:
            Mincount = count
        return
    if not count or not Mincount:
        Mincount = 0
        return
    for x in range(W):
        c, newMap = droptheball(x,Map)
        if c:
            dfs(i+1,newMap,count-c)

def Mapcopy(Map):
    retMap = [[0]*H for _ in range(W)]
    for w in range(W):
            retMap[w] = Map[w][:]
    return retMap

def rotate(Map):
    retMap = [[0]*H for _ in range(W)]
    count = 0
    for h in range(H):
        for w in range(W):
            retMap[w][h] = Map[h][W-w-1]
            if retMap[w][h]:
                count += 1
    return count, retMap

for tc in range(1,int(input())+1):
    N,W,H = map(int, input().split())
    Map = [list(map(int,input().split())) for _ in range(H)]
    count, Map = rotate(Map)
    Mincount = count
    dfs(0,Map,count)
    print(f'#{tc}', Mincount)
