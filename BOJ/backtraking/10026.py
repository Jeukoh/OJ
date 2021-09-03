import sys; readline = sys.stdin.readline
N = int(readline())
Map = [readline().rstrip() for _ in range(N)]

#위 왼 아래 오른
dx = (-1,0,1,0)
dy = (0,-1,0,1)

# 정상
anw1 = 0
visited = [[True]*N for _ in range(N)]


for x in range(N):
    for y in range(N):
        if visited[x][y]:
            visited[x][y] = False
            cl = Map[x][y]
            stack = [[x,y]]
            anw1 += 1
            while stack:
                tmp_x,tmp_y = stack.pop()
                for _ in range(4):
                    new_x = tmp_x+ dx[_]
                    new_y = tmp_y+ dy[_]
                    if 0 <= new_x < N and 0 <= new_y < N and visited[new_x][new_y] and Map[new_x][new_y] == cl:
                        stack.append([new_x,new_y])
                        visited[new_x][new_y] = False
                #print(x, y, stack)
anw2 = 0
visited = [[True]*N for _ in range(N)]
for idx, value in enumerate(Map):
    Map[idx] = value.replace('G','R')
for x in range(N):
    for y in range(N):
        if visited[x][y]:
            visited[x][y] = False
            cl = Map[x][y]
            stack = [[x,y]]
            anw2 += 1
            while stack:
                tmp_x,tmp_y = stack.pop()
                for _ in range(4):
                    new_x = tmp_x+ dx[_]
                    new_y = tmp_y+ dy[_]
                    if 0 <= new_x < N and 0 <= new_y < N and visited[new_x][new_y] and Map[new_x][new_y] == cl:
                        stack.append([new_x,new_y])
                        visited[new_x][new_y] = False
                #print(x,y,stack)

print(anw1, anw2)