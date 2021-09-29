import sys; readline = sys.stdin.readline
from pprint import pprint
N = int(input())
adj = [list(map(int,readline().split())) for _ in range(N)]

# k를 거쳐서
for k in range(N):
    # x에서
    for x in range(N):
        # y로 갈 수 있나?
        for y in range(N):
            if adj[x][k] and adj[k][y]:
                adj[x][y] = 1

print('\n'.join(' '.join(str(x) for x in y) for y in adj))