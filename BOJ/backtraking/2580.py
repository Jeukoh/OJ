import sys; readline = sys.stdin.readline

visit_box = [[True]*9 for _ in range(10)]
visit_row = [[True]*9 for _ in range(10)]
visit_col = [[True]*9 for _ in range(10)]
list_zero = []
Map = []

for i in range(9):
    tmp = list(map(int,readline().split()))
    Map.append(tmp)
    for j in range(9):
        if tmp[j] == 0:
            list_zero.append([i,j])
        else:
            visit_box[tmp[j]][(i//3)*3+j//3] = False
            visit_row[tmp[j]][i] = False
            visit_col[tmp[j]][j] = False

N = len(list_zero)


def dfs(k):
    if k == N:
        print('\n'.join(' '.join(str(x) for x in y) for y in Map))
        sys.exit()

    x,y = list_zero[k]
    for n in range(1,10):
        if visit_box[n][(x//3)*3+y//3] and visit_row[n][x] and visit_col[n][y]:
            visit_box[n][(x // 3) * 3 + y // 3] = False
            visit_row[n][x] = False
            visit_col[n][y] = False
            Map[x][y] = n
            dfs(k+1)
            Map[x][y] = 0
            visit_box[n][(x // 3) * 3 + y // 3] = True
            visit_row[n][x] = True
            visit_col[n][y] = True

dfs(0)

