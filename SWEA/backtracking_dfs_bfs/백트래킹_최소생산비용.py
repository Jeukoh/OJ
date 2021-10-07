def rec(i,s):
    global anw
    if s >= anw:
        return
    if i == N and s < anw:
        anw = s
    for x in range(N):
        if visited[x]:
            visited[x] = False
            rec(i+1,s+cost[i][x])
            visited[x] = True

for tc in range(1,int(input())+1):
    N = int(input())
    cost = [list(map(int,input().split())) for _ in range(N)]
    anw = sum(cost[i][i] for i in range(N))
    visited = [True]*N
    rec(0,0)
    print(f'#{tc}', anw)