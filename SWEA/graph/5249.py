from collections import defaultdict
from heapq import *

for tc in range(1,int(input())+1):
    V, E = map(int,input().split())
    V = V+1
    adj = defaultdict(list)
    for _ in range(E):
        a,b,w = map(int,input().split())
        adj[a].append([w,b])
        adj[b].append([w,a])

    Tree_node = set([0])
    cand_list = adj[0]
    heapify(cand_list)
    MST = 0
    while cand_list:
        print(Tree_node)
        print(cand_list)
        w, node = heappop(cand_list)
        if node not in Tree_node:
            Tree_node.add(node)
            MST += w

            for e in adj[node]:
                if e[1] not in Tree_node:
                    heappush(cand_list,e)

    print(f'#{tc}',MST)