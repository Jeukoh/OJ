from collections import deque

def bfs(S):
    Q = deque([S])
    cnt = 0
    while Q:
        x = Q.popleft()
        cnt += 1
        for v in adj[x]:
            Q.append(v)
    return cnt

for tc in range(1,int(input())+1):
    E, N = map(int,input().split())
    adj = [[] for _ in range(E+2)]
    adj_in = list(map(int,input().split()))
    for i in range(E):
        adj[adj_in[2*i]].append(adj_in[2*i+1])
    print(f'#{tc}', bfs(N))