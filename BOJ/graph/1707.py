import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
for tc in range(int(input())):
    def dfs(v, col):
        visited[v] = col
        for adj_v in adj[v]:
            if visited[adj_v] == 0:
                if not dfs(adj_v,-col):
                    return False
            elif visited[adj_v] == visited[v]:
                return False
        return True


    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    visited = [0]*(V+1)
    for _ in range(E):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)


    anw = True
    for i in range(1, V + 1):
        if visited[i] == 0:
            anw = dfs(i, 1)
            if not anw:
                break
    if anw:
        print('YES')
    else:
        print('NO')
