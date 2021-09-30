for tc in range(1, int(input())+1):
    N, M = map(int,input().split())
    weights = list(map(int,input().split()))
    trucks = list(map(int,input().split()))
    trucks.sort()
    weights.sort()
    anw = 0
    while trucks:
        truck = trucks.pop()


        while weights and weights[-1] > truck:
            weights.pop()

        if weights:
            anw += weights.pop()

    print(f'#{tc} {anw}')