def find_root(x):
    if x != root[x]:
        root[x] = find_root(root[x])
    return root[x]

def link(x, y):

    a, b = find_root(x), find_root(y)
    if rank[a] > rank[b]:
        root[b] = a
    elif rank[b] > rank[a]:
        root[a] = b
    else:
        root[b] = a
        rank[a] += 1


def union(x, y):
    link(find_root(x), find_root(y))


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    rank = [0] * (N + 1)
    root = [i for i in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        union(a, b)
    for idx in range(1, N + 1):
        find_root(idx)


    print(f'#{tc}', len(set(root)) - 1)
