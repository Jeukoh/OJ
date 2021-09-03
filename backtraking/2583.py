import sys; readline = sys.stdin.readline
Y, X, K = map(int,readline().split())
rec_list = [list(map(int,readline().split())) for _ in range(K)]

Map = [[True]*Y for _ in range(X)]

for i in rec_list:
    for x in range(i[0],i[2]):
        for y in range(i[1],i[3]):
            Map[x][y] = False


dx = (-1,0,1,0)
dy = (0,-1,0,1)

anw_l = []
for x in range(X):
    for y in range(Y):
        if Map[x][y]:
            Map[x][y] = False
            anw = 0
            stack = [[x,y]]
            while stack:
                tmp_x, tmp_y = stack.pop()
                anw += 1
                for _ in range(4):
                    new_x, new_y = tmp_x+dx[_], tmp_y+dy[_]
                    if 0 <= new_x < X and Y > new_y >= 0 and Map[new_x][new_y]:
                        stack.append([new_x,new_y])
                        Map[new_x][new_y] = False

            anw_l.append(anw)
anw_l.sort()
print(len(anw_l))
print(*anw_l)