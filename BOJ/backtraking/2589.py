import sys; readline = sys.stdin.readline
from collections import deque
X, Y = map(int,readline().split())
Map = [readline().rstrip() for _ in range(X)]

dx = (-1,0,1,0)
dy = (0,-1,0,1)

visited = [[0]*Y for _ in range(X)]

def bfs(s:list):
    stack = deque([s])
    anw = 0
    while stack:
        flag = True
        x, y = stack.popleft()
        for _ in range(4):
            new_x = x + dx[_]
            new_y = y + dy[_]
            if X > new_x >= 0 and Y > new_y >= 0 and not visited[new_x][new_y] and Map[new_x][new_y] == 'L':
                stack.append([new_x,new_y])
                visited[new_x][new_y] = visited[x][y] + 1
                flag = False
        if flag:
            anw = max(anw,visited[x][y]-1)
    return anw

anw = 0
for x in range(X):
    for y in range(Y):
        if Map[x][y] == 'L':
            if x >= 1 and x < X-1 and Map[x-1][y] == "L" and Map[x+1][y] == "L":
                continue
            if y >= 1 and y < Y-1 and Map[x][y-1] == "L" and Map[x][y+1] == "L":
                continue
            visited = [[0] * Y for _ in range(X)]
            visited[x][y] = 1
            anw = max(anw,bfs([x,y]))

print(anw)

