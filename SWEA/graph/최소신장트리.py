from heapq import *

def find(x):
    if x == root[x]:
        return x
    root[x] = find(root[x])
    return root[x]

def union(x,y):
    a,b = find(x), find(y)
    root[b] = a

for tc in range(1, int(input()) + 1):
    V, E = map(int,input().split())

    root = [i for i in range(V+1)]
    adjs = []
    for _ in range(E):
        n1,n2,w = map(int,input().split())
        heappush(adjs, [w,n1,n2])


    cnt = 0
    anw = 0
    while cnt != V:

        w,n1,n2 = heappop(adjs)

        if find(n1) == find(n2):
            continue
        else:
            anw += w
            union(n1,n2)
            cnt += 1

    print(f'#{tc}', anw)