for tc in range(1,int(input())+1):
    N, M, K = map(int,input().split())
    sonnom = list(map(int,input().split()))
    sonnom.sort(reverse=True)
    fish = 0
    anw = 'Possible'
    for t in range(0,sonnom[0]+M,M):
        while sonnom and sonnom[-1] < t:
            sonnom.pop()
            fish -= 1
        if fish < 0:
            anw = 'Impossible'
            break
        if t != 0:
            fish += K
        while sonnom and sonnom[-1] <= t:
            sonnom.pop()
            fish -= 1

        if not sonnom:
            break


    print(f'#{tc}', anw)
