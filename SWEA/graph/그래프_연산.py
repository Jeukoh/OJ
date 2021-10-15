from collections import deque

const = 1000000
for tc in range(1,int(input())+1):
    N, M = map(int,input().split())

    Q = deque([[N,0]])
    visited = set([N])
    while Q:
        V, C = Q.popleft()
        if V == M:
            break

        if V+1 <= const and V+1 not in visited:
            visited.add(V+1)
            Q.append([V+1,C+1])

        if 1 <= V-1 and V-1 not in visited:
            visited.add(V-1)
            Q.append([V-1,C+1])

        if 2*V <= const and 2*V not in visited:
            visited.add(2*V)
            Q.append([2*V,C+1])

        if 1 <= V-10 and V-10 not in visited:
            visited.add(V-10)
            Q.append([V-10,C+1])


    print(f'#{tc}', C)