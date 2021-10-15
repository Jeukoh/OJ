from heapq import *
from collections import defaultdict

for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    adj = defaultdict(list)

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1].append([w,n2])

    d = [float('inf')] * (V+1)


    Q = [[0,0]]

    while Q:
        now_w, node = heappop(Q)

        if d[node] < now_w:
            continue

        for next_w, next_node in adj[node]:
            if next_w+now_w < d[next_node]:
                d[next_node] = next_w+now_w
                heappush(Q, [next_w+now_w, next_node])


    print(f'#{tc}', d[-1])