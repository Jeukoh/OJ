
# 프림 알고리즘 -> V**2 라서 이 경우 크루스칼보다 빠름

for tc in range(1, int(input()) + 1):
    N = int(input())
    xs = list(map(int,input().split()))
    ys = list(map(int,input().split()))
    E = float(input())
    inf = float('inf')
    Tree = [False]*N
    dist = [inf]*N
    dist[0] = 0
    anw = 0
    for _ in range(N):
        min_idx, min_v = -1, inf
        for idx in range(N):
            if not Tree[idx] and min_v > dist[idx]:
                min_idx = idx
                min_v = dist[idx]
        Tree[min_idx] = True
        anw += min_v
        for n_idx in range(N):
            if not Tree[n_idx]:
                D = E*((xs[n_idx]-xs[min_idx])**2 + (ys[n_idx]-ys[min_idx])**2)
                if D < dist[n_idx]:
                    dist[n_idx] = D

    print(f'#{tc}', round(anw))