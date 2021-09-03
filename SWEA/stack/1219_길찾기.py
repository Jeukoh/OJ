while True:
    try:
        tc, V = map(int,input().split())
    except EOFError:
        break

    i_list = list(map(int,input().split()))
    Map = [[-1]*2 for _ in range(100)]
    for _ in range(0,V):
        if Map[i_list[2*_]][0] == -1:
            Map[i_list[2*_]][0] = i_list[2*_+1]
        else:
            Map[i_list[2 * _]][1] = i_list[2 * _ + 1]




    anw = 0
    stack = [0]
    visit = [True]*100
    while stack:
        i = stack.pop()
        visit[i] = False
        if i == 99:
            anw = 1
            break
        for _ in range(2):
            if Map[i][_] != -1 and visit[Map[i][_]]:
                stack.append(Map[i][_])

    print(f'#{tc} {anw}')