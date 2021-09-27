import sys; readline = sys.stdin.readline
from collections import defaultdict, deque
N = int(input())
root = list(map(int,readline().split()))
K = int(input())
root_node = []
adj = defaultdict(list)
for idx,v in enumerate(root):
    if v == -1:
        root_node.append(idx)
    else:
        if v == K or idx == K:
            continue
        adj[v].append(idx)

def bfs(root_node):
    cnt = 0
    Q = deque(list(filter(lambda x: x!=K, root_node)))
    while Q:
        v = Q.popleft()
        if adj.get(v):
            for vv in adj.get(v):
                Q.append(vv)
        else:
            cnt += 1
    return cnt
print(bfs(root_node))
