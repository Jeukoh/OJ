def bfs():
    anw = 0
    global stack
    while stack:
        tmp_stack = []
        for v in stack:
            Map[v[0]][v[1]] = -1
            for _ in range(8):
                nx, ny = v[0]+dx[_], v[1]+dy[_]
                if  X>nx>=0 and Y>ny>=0 and Map[nx][ny] > 0:
                    Map[nx][ny] -= 1
                    if Map[nx][ny] == 0:
                        tmp_stack.append([nx,ny])

        stack = tmp_stack[:]
        anw += 1
    return anw

import sys; readline = sys.stdin.readline
X, Y = map(int,readline().split())

Map = [list(readline().rstrip()) for _ in range(X)]


dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

stack = []
for x in range(X):
    for y in range(Y):
        if Map[x][y] == '.':
            Map[x][y] = 0
            stack.append([x,y])
        else:
            Map[x][y] = int(Map[x][y])

anw = bfs()
print(anw-1)