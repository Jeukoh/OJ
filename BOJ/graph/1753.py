import sys; readline = sys.stdin.readline
from collections import defaultdict
import heapq
V, E = map(int,readline().split())
S = int(readline().rstrip())
adj = defaultdict(list)

for _ in range(E):
    a,b,w = map(int,readline().split())
    adj[a].append([w,b])

def dijkstra(S):
    D = [float('inf')]*(V+1)
    D[S] = 0
    cand = []

    heapq.heappush(cand,[0,S])


    while cand:
        dist, cur = heapq.heappop(cand)

        if D[cur] < dist:
            continue
        for w, v in adj[cur]:
            now_D = w + D[cur]
            if now_D < D[v]:
                heapq.heappush(cand, [now_D,v])
                D[v] = now_D
    return D

D = dijkstra(S)
for i in range(1,V+1):
    if D[i] == float('inf'):
        print('INF')
        continue
    print(D[i])