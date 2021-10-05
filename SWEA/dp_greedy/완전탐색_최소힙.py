for tc in range(1,int(input())+1):
    N = int(input())
    Map = [list(map(int,input().split())) for _ in range(N)]

    for x in range(N):
        for y in range(N):
            if not x and not y:
                continue
            if not x:
                Map[x][y] += Map[x][y-1]
                continue
            if not y:
                Map[x][y] += Map[x-1][y]
                continue

            Map[x][y] += min(Map[x-1][y],Map[x][y-1])


    print(f'#{tc}', Map[-1][-1])