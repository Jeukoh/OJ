for tc in range(1,int(input())+1):
    D, N = map(int,input().split())
    horse = [list(map(int,input().split())) for _ in range(N)]
    # K, S
    # 거 속*시
    anw = D
    t_max = 0
    for i in horse:
        t_max =  max(t_max,(D-i[0])/i[1])

    v = D/t_max
    print(f'#{tc}',"{:.8f}".format(v))
