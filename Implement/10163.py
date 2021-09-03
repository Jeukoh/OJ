import sys; readline=sys.stdin.readline
N = int(input())
paper_list = []
min_x,min_y,max_x,max_y = 1002,1002,0,0
for _ in range(N):
    paper_list.append(list(map(int,readline().split())))
    min_x, min_y = min(min_x,paper_list[-1][0]), min(min_y,paper_list[-1][1])
    max_x, max_y = max(max_x,paper_list[-1][0]+paper_list[-1][2]), max(max_y,paper_list[-1][1]+paper_list[-1][3])

Map = [[0]*(max_y-min_y+1) for _ in range(max_x-min_x+1)]
for _ in range(1,N+1):
    x,y,Dx,Dy = paper_list[_-1]
    for dx in range(Dx):
        for dy in range(Dy):
            Map[x-min_x+dx][y-min_y+dy] = _

count_list = [0]*N
for x in range(max_x-min_x+1):
    for y in range(max_y-min_y+1):
        if Map[x][y]:
            count_list[Map[x][y]-1] += 1


print(*count_list,sep='\n')