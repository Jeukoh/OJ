import sys; readline = sys.stdin.readline
from collections import deque
dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(Map):
    Sol = 123456789
    cnt = 0
    Q = deque([Map])
    visited = {Map:0}
    tmp_Q = []
    while Q:
        Map = Q.popleft()
        if Map == Sol:
            return visited[Sol]
        k = str(Map)
        kk = k.index('9')
        x, y = kk//3, kk%3
        for _ in range(4):
            nx, ny = x + dx[_], y + dy[_]
            if 3>nx>=0 and 3>ny>=0:
                f_idx = 3*nx+ny
                ret_Map = list(k)
                ret_Map[kk], ret_Map[f_idx] = ret_Map[f_idx], ret_Map[kk]
                M_c = int(''.join(ret_Map))
                if not visited.get(M_c):
                    visited[M_c] = visited[Map] + 1
                    Q.append(M_c)
    return -1

Map = ''
for _ in range(3):
    Map += readline().replace(' ','').rstrip('\n')
Map = int(Map.replace('0','9'))
print(bfs(Map))

