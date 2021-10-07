def rec(i, s):
    global anw
    if i == N:
        anw = s
        return
    if s * remains[i] <= anw:
        return
    for x in range(N):
        if visited[x] and s * cost[i][x] / 100 > anw:
            visited[x] = False
            rec(i + 1, s * cost[i][x] / 100)
            visited[x] = True


anws = []
for tc in range(1, int(input()) + 1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    anw = 100
    remains = []
    remain = 1
    for x in range(N):
        anw *= cost[x][x] / 100
        remain *= max(cost[x]) / 100
    for x in range(N):
        remains.append(remain)
        remain /= max(cost[x]) / 100
    visited = [True] * N
    rec(0, 100)
    anws.append('#{} {:6f}'.format(tc, anw * 1))

print('\n'.join(anws))