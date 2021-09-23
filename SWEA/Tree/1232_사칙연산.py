def getcal(idx):
    if isinstance(tree[idx],int):
        return tree[idx]
    le = getcal(child[idx][0])
    ri = getcal(child[idx][1])
    tree[idx] = eval(str(le)+tree[idx]+str(ri))
    return tree[idx]

for tc in range(1,11):
    V = int(input())
    tree = [[] for _ in range(V+1)]
    child = {}
    for _ in range(V):
        tmp = input().split()
        if tmp[1].isdigit():
            tree[int(tmp[0])] = int(tmp[1])
        else:
            tree[int(tmp[0])] = tmp[1]
            child[int(tmp[0])] = [int(tmp[2]),int(tmp[3])]
    getcal(1)
    print(f'#{tc}', int(tree[1]))