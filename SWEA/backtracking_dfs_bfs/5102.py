def bfs(S,F):
    anw = 0
    stack = [S]
    visited = [True]*(V+1)
    while stack:
        tmp = []
        for s in stack:
            for idx,v in enumerate(E_map[s]):
                if v != 0:
                    if visited[idx]:
                        if idx == F:
                            return anw+1
                        tmp.append(idx)
                        visited[idx] = False
        stack = tmp[:]
        anw += 1
    return 0

for tc in range(1,int(input())+1):
    V, E = map(int,input().split())
    E_map = [[0]*(V+1) for _ in range(V+1)]

    for _ in range(E):
        a, b = map(int,input().split())
        E_map[a][b] = 1
        E_map[b][a] = 1

    S, F = map(int,input().split())

    print(f'#{tc}', bfs(S,F))