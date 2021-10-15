from heapq import *
from collections import defaultdict

for tc in range(1, int(input()) + 1):
    V,E,X = map(int, input().split())
    adj = defaultdict(list)
    adj2 = defaultdict(list)
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1].append([w,n2])
        adj2[n2].append([w,n1])

    d = [float('inf')] * (V+1)
    d2 = [float('inf')] * (V + 1)


    Q = [[0,X]]
    d[X] = 0

    while Q:
        now_w, node = heappop(Q)

        if d[node] < now_w:
            continue

        for next_w, next_node in adj[node]:
            if next_w+now_w < d[next_node]:
                d[next_node] = next_w+now_w
                heappush(Q, [next_w+now_w, next_node])

    Q = [[0,X]]
    d2[X] = 0

    while Q:
        now_w, node = heappop(Q)

        if d2[node] < now_w:
            continue

        for next_w, next_node in adj2[node]:
            if next_w+now_w < d2[next_node]:
                d2[next_node] = next_w+now_w
                heappush(Q, [next_w+now_w, next_node])

    anw = 0

    for i in range(1,V+1):
        anw = max(anw,d[i] + d2[i])

    #print(d,d2)

    print(f'#{tc}', anw)