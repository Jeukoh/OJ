import sys; readline = sys.stdin.readline
from pprint import pprint

Map = [readline().rstrip() for _ in range(5)]
S_loc = []
for x in range(5):
    for y in range(5):
        if Map[x][y] == 'S':
            S_loc.append([x,y])

anw = 0
safe_set = []
visited = [[True]*5 for _ in range(5)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]

def setsafe(x,y):
    for _ in range(4):
        nx, ny = x+dx[_], y+dy[_]
        safe_set.append((nx,ny))

def delsafe(x,y):
    for _ in range(4):
        safe_set.pop()


query_set = set()

def dfs(i,Y):
    global anw

    if Y >= 4:
        return

    if i == 7:
        query_set.add(tuple(sorted(stack)))
        return False

    for x,y in safe_set:
        if 5 > x >= 0 and 5 > y >= 0 and visited[x][y]:
            visited[x][y] = False
            setsafe(x, y)
            stack.append((x,y))
            if Map[x][y] == 'S':
                dfs(i+1,Y)
            else:
                dfs(i + 1, Y + 1)
            stack.pop()
            visited[x][y] = True
            delsafe(x, y)


stack = []
for x,y in S_loc:
    setsafe(x,y)
    visited[x][y] = False
    stack.append((x,y))
    dfs(1,0)
    delsafe(x,y)
    stack.pop()



print(len(query_set))