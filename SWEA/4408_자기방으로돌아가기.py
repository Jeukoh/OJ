for tc in range(1,int(input())+1):
    Map = [0]*201
    max_v = 0
    N = int(input())
    for _ in range(N):
        a, b = map(int,input().split())
        a = (a+1)//2
        b = (b+1)//2
        #swap
        if a > b:
            a, b = b, a
        for idx in range(a,b+1):
            Map[idx] += 1

    for i in Map:
        if max_v < i:
            max_v = i

    print(f'#{tc} {max_v}')