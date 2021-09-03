
T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split())
    Map = [[0]*(V+1) for _ in range(V+1)]
    for __ in range(E):
        a, b = map(int,input().split())
        Map[a][b] = 1
    s, e = map(int,input().split())


    anw = 0
    i = s
    stack = [i]
    visit = [True]*(V+1)
    while stack:
        i = stack.pop()
        visit[i] = False
        if i == e:
            anw = 1
            break

        for _ in range(1,V+1):
            if Map[i][_] and visit[_]:
                stack.append(_)

    print(f'#{tc} {anw}')