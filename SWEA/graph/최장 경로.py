from collections import defaultdict, deque

# def bfs(i):
#     visited = [True]*(N+1)
#     visited[i] = False
#     Q = deque([[i,1]])
#     while Q:
#         node, cnt = Q.popleft()
#         for nv in adj[node]:
#             if visited[nv]:
#                 visited[nv] = False
#                 Q.append([nv,cnt+1])
#
#     return node, cnt


def dfs(s,i,cnt):

    isLeaf = True
    #print(s,i,cnt)
    for nv in adj[i]:
        if visited[nv]:
            visited[nv] = False
            dfs(s,nv,cnt+1)
            visited[nv] = True
            isLeaf = False

    if isLeaf:
        cand_anw[s] = max(cand_anw[s],cnt)
        cand_anw[i] = max(cand_anw[i],cnt)

for tc in range(1,int(input())+1):
    N, M = map(int,input().split())

    adj = defaultdict(list)
    for _ in range(M):
        a, b = map(int,input().split())
        adj[a].append(b)
        adj[b].append(a)

    cand_anw = [0]*(N+1)

    for node in range(1,N+1):
        visited = [True]*(N+1)
        visited[node] = False
        dfs(node,node,1)


    print(f'#{tc}',max(cand_anw))