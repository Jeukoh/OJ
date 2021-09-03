import sys; readline = sys.stdin.readline
N = int(input())

line = {x:[] for x in range(2*N-1)}
Map = [list(map(int,readline().split())) for _ in range(N)]

for x in range(N):
    for y in range(N):
        if Map[x][y]:
            line[x+y].append([x,y])

rd = [True]*(2*N-1)

max_anw = [0,0]
# 0,0 부터 0 -.  ru으로 채움 2n-1까지
def dfs(i,anw):
    if i%2:
        if anw > max_anw[0]:
            max_anw[0] = anw
    else:
        if anw > max_anw[1]:
            max_anw[1] = anw
    if i >= 2*N-1:
        return
    for v in line[i]:
        if rd[v[0]-v[1]+(N-1)]:
            rd[v[0]-v[1]+(N-1)] = False
            dfs(i+2,anw+1)
            rd[v[0]-v[1]+(N-1)] = True
    dfs(i+2,anw)

dfs(0,0)
dfs(1,0)

print(sum(max_anw))