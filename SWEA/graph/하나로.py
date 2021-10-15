from heapq import *
from itertools import combinations as comb

# 크루스칼 알고리즘 -> 시간복잡도 Elog(E) E가 매우 커서 (V**2)라서 2(V**2)log(V)

def find(x):
    if x == root[x]:
        return x
    root[x] = find(root[x])
    return root[x]



def union(x,y):
    a, b = find(x), find(y)
    if rank[a] > rank[b]:
        root[b] = a
    elif rank[b] > rank[a]:
        root[a] = b
    else:
        root[b] = a
        rank[a] += 1

for tc in range(1, int(input()) + 1):

    N = int(input())
    xs = list(map(int,input().split()))
    ys = list(map(int,input().split()))
    E = float(input())

    root = [i for i in range(N)]
    rank = [0]*N
    adjs = []
    for x, y in comb(range(N),2):
        w = E*((xs[x]-xs[y])**2 + (ys[x]-ys[y])**2)
        heappush(adjs, [w,x,y])


    cnt = 0
    anw = 0
    while cnt != (N-1):
        w,n1,n2 = heappop(adjs)
        if find(n1) == find(n2):
            continue
        else:
            anw += w
            union(n1,n2)
            cnt += 1

    print(f'#{tc}', round(anw))