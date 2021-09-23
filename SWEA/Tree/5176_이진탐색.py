import math

def inserttree(idx):
    global cnt

    if idx <= V:
        inserttree(2*idx)
        tree[idx] = cnt
        cnt += 1
        inserttree(2*idx+1)

for tc in range(1,int(input())+1):
    V = int(input().rstrip())
    tree = [[] for _ in range(V+1)]
    cnt = 1

    inserttree(1)

    print(f'#{tc}', tree[1], tree[V//2])