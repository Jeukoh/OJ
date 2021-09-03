import sys; readline = sys.stdin.readline
import heapq
def Prim(S):
    visited = [False]+[True]*(V)
    Q = [[0,S]]
    anw = 0
    while Q:
        cost, treeidx = heapq.heappop(Q)
        visited[treeidx] = False
        anw += cost
        if not any(visited[1:]):
            break
        for value in adj[treeidx]:
            if visited[value[1]]:
                heapq.heappush(Q,value)
    print(anw)

V, E = map(int,input().split())
adj = {i:[] for i in range(1,V+1)}
for _ in range(E):
    a,b,c = map(int,input().split())
    adj[a].append([c,b])
    adj[b].append([c,a])
Prim(1)
