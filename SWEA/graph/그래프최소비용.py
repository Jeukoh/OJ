dx = (-1,0,1,0)
dy = (0,-1,0,1)

from heapq import *
from collections import defaultdict
for tc in range(1, int(input()) + 1):
    N = int(input())
    Map = [list(map(int,input().split())) for _ in range(N)]


    Q = []
    # weights, Node
    heappush(Q, [0,0,0])
    d = [[float('inf')]*N for _ in range(N)]

    while Q:
        W, x, y = heappop(Q)

        if d[x][y] < W:
            continue

        for _ in range(4):
            nx, ny = x+dx[_], y+dy[_]

            if 0 <= nx < N and 0 <= ny < N:

                new_W = W + 1 + max(Map[nx][ny] - Map[x][y],0)

                if new_W < d[nx][ny]:
                    d[nx][ny] = new_W
                    heappush(Q, [new_W, nx, ny])

    print(f'#{tc}', d[-1][-1])