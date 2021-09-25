from itertools import permutations

for tc in range(1,int(input())+1):
    N = int(input())
    Map = [list(map(int,input().split())) for _ in range(N)]

    permulist = permutations([i for i in range(1,N)],N-1)

    min_v = float('inf')
    for x in permulist:
        v = 0
        for idx in range(N):
            if idx == 0:
                start = 0
                end = x[idx]
            elif idx == N-1:
                start = x[idx-1]
                end = 0
            else:
                start = x[idx-1]
                end = x[idx]
            v += Map[start][end]
        min_v = min(v,min_v)
    print(f'#{tc}',min_v)