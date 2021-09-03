T = int(input())
for t in range(1,T+1):
    N, K = map(int,input().split())
    Map = [list(map(int,input().split())) for _ in range(N)]

    max = 0
    for r in range(N-K+1):
        for c in range(N-K+1):
            tmp = 0
            for dx in range(K):
                for dy in range(K):
                    tmp += Map[r+dx][c+dy]

            if max < tmp:
                max = tmp


    print(f'#{t} {max}')