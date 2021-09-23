def heapsum(idx):

    if idx > V:
        return 0
    if tree[idx]:
        return tree[idx]

    lev = heapsum(2*idx)
    riv = heapsum(2*idx+1)
    tree[idx] = lev+riv
    return tree[idx]

for tc in range(1,int(input())+1):
    V, M, L = map(int,input().split())
    tree = [[] for _ in range(V+1)]
    for _ in range(M):
        idx, v = map(int,input().split())
        tree[idx] = v

    heapsum(1)
    print(f'#{tc}', tree[L])