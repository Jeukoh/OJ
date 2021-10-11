import sys; readline=sys.stdin.readline
N,M = map(int,readline().split())
bibun = {}
for _ in range(N):
    tmp = readline().split()
    bibun[tmp[0]] = tmp[1]
anw = [0]*M
for _ in range(M):
    anw[_] = bibun[readline().strip()]
print('\n'.join(anw))