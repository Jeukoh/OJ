import sys
from collections import deque
import copy
def bfs(Q,mp,safecnt): # 벽 다 쌓은 후 바이러스 위치 Q와 카피댄 맵을 받아서 퍼트리고 안전공간 수 반환
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    r1 = safecnt
    #print(Q,mp)
    while Q:
        #print(Q,safecnt)
        x,y = Q.popleft()
        for _ in range(4):
            #print(Q,_)
            nx = x+dx[_]
            ny = y+dy[_]
            if 0 <= nx and nx < N and 0<= ny and ny < M and mp[nx][ny]==0:
                mp[nx][ny] = 2
                Q.append([nx,ny])
                r1 -= 1
    return r1
def dfs(xy,cnt): # 벽을 3개 쌓으면 bfs, 모든 경우에 벽을 쌓는다. 중복 조심.
    global res
    if cnt==3:
        cpQ = copy.deepcopy(Q)
        cpmp = copy.deepcopy(mp)
        tmp = bfs(cpQ,cpmp,safecnt)
        if res < tmp:
            res = tmp
        return
    for I in range(xy,N*M):
        x = I//M
        y = I%M
        if mp[x][y] == 0:
            mp[x][y] = 1
            dfs(xy+1,cnt+1)
            mp[x][y] = 0

readr = sys.stdin.readline
N, M = map(int,readr().split())
mp = []
Q = deque()
safecnt = N*M
res = -1
for x in range(N):
    mp.append(list(map(int,readr().split())))
    for y, n in enumerate(mp[x]):
        if n==2:
            Q.append([x,y])
            safecnt -= 1
        if n==1:
            safecnt -= 1

dfs(0,0)
print(res-3)

