T = 10
for t in range(1,T+1):
    input()
    N = 100

    Map = [input() for _ in range(N)]

    anw1 = 0
    anw2 = 0
    # 가로 검사
    for M in range(100, 0, -1):
        for i in range(N):
            for j in range(N-M+1): # 시작 점 Map[i][j 0~N-M+1]
                for k in range(M//2+M%2):
                    if Map[i][j+k] != Map[i][j+M-1-k]:
                        break
                else:
                    anw1 = M
                    break
            if anw1:
                break
        if anw1:
            break

    # 세로 검사
    for M in range(100, 0, -1):
        if M < anw1:
            break
        for j in range(N):
            for i in range(N - M + 1):  # 시작 점 Map[i][j 0~N-M+1]
                for k in range(M // 2+M%2):
                    if Map[i+k][j] != Map[i+M-1-k][j]:
                        break
                else:
                    anw2 = M
                    break
            if anw2:
                break
        if anw2:
            break

    #print(anw1, anw2)

    print(f'#{t} {max(anw1, anw2)}')