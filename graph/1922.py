def Prime(s):
    min_adj = [0]+[sys.maxsize]*N
    visit = [False]*(N+1)
    visit[0] = True
    root = [i for i in range(N+1)]

    min_adj[s] = 0
    anw = 0

    for _ in range(N):
        min_idx = -1
        tmp_min = sys.maxsize

        # 비트리 정점 중 가중치가 최소인 정점 선택
        for i in range(1,N+1):
            if not visit[i] and min_adj[i] < tmp_min:
                tmp_min = min_adj[i]
                min_idx = i
        visit[min_idx] = True
        # 방문.

        # 선택된 정점에 연결된 간선 확인
        # 현재 자기 최소 가중치보다 작은
        for adj_idx, adj_value in enumerate(adj[min_idx]):
            if not visit[adj_idx] and adj_value < min_adj[adj_idx]:
                min_adj[adj_idx] = adj_value
                root[adj_idx] = min_idx

    for idx, r in enumerate(root):
        if idx==r: continue
        anw += adj[idx][r]
    return anw

import sys; readline = sys.stdin.readline
N = int(input())
M = int(input())

adj = [[sys.maxsize]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, w = map(int,readline().split())
    if a != b:
        adj[a][b] = w
        adj[b][a] = w

tree = Prime(1)
print(tree)
