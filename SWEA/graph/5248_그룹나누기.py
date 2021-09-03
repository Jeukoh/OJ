def find_root(x):
    if x != root[x]:
        root[x] = find_root(root[x])
    return root[x]

def link(a,b):
    if rank[a] > rank[b]:
        root[b] = a
        return a
    elif rank[b] > rank[a]:
        root[a] = b
        return b
    else:
        root[b] = a
        rank[a] += 1
        return b


def union(x,y):
    link(find_root(x),find_root(y))




for tc in range(1,int(input())+1):
    N, M = map(int,input().split())
    rank = [0]*(N+1)
    root = [i for i in range(N+1)]
    M_list = list(map(int,input().split()))

    for idx in range(M):
        union(M_list[2*idx],M_list[2*idx+1])
    for idx in range(1,N+1):
        find_root(idx)

    print(f'#{tc}',len(set(root))-1)
