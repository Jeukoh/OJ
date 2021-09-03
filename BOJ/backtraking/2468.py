import sys; readline = sys.stdin.readline
N = int(readline())
Map = [list(map(int,readline().split())) for _ in range(N)]
min_h = 100
max_h = 0
for i in Map:
    max_h = max(max_h,max(i))
    min_h = min(min_h,min(i))

dx = (-1,0,1,0)
dy = (0,-1,0,1)

max_anw = 0

for h in range(min_h-1,max_h+1):
    # h 아래는 잠겨
    visited = [[True]*N for _ in range(N)]
    #구역 수
    anw = 0
    for x in range(N):
        for y in range(N):
            if visited[x][y] and Map[x][y] > h:
                anw += 1
                visited[x][y] = False
                stack = [[x,y]]
                while stack:
                    tmp_x, tmp_y = stack.pop()
                    for _ in range(4):
                        new_x = tmp_x + dx[_]
                        new_y = tmp_y + dy[_]
                        if N > new_x >= 0 and N > new_y >= 0 and visited[new_x][new_y] and Map[new_x][new_y] > h:
                            stack.append([new_x,new_y])
                            visited[new_x][new_y] = False

    max_anw = max(max_anw,anw)

print(max_anw)