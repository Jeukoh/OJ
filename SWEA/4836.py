T = int(input())

for t in range(1,1+T):
    Map = [[0]*10 for _ in range(10)]
    N = int(input())

    purple = 0

    for _ in range(N):
        r1,c1,r2,c2,color = map(int,input().split())

        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                Map[i][j] += color
                if Map[i][j] == 3:
                    purple += 1

    print(f'#{t} {purple}')