for tc in range(1,int(input())+1):
    N, M = map(int,input().split())
    cheese = list(map(int,input().split()))
    fire = [i for i in range(N)]

    cur = 0
    pizza_cur = N
    while cheese.count(0) < M-1:
        cheese[fire[cur]] //= 2
        if not cheese[fire[cur]]:
            fire[cur] = pizza_cur
            pizza_cur = (pizza_cur+1)%M
        cur = (cur+1)%N


    for idx in range(M):
        if cheese[idx]:
            anw = idx+1
            break
    print(f'#{tc}', anw)