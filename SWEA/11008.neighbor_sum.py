T = int(input())

for t in range(1,1+T):
    N = int(input())
    N_list = []

    for _ in range(N):
        N_list.append(list(map(int,input().split())))

    d = [(-1,0),(1,0),(0,-1),(0,1)]
    max_idx = [0,0]
    max_value = 0
    for i in range(N):
        for j in range(N):
            tmp = 0
            for _ in range(4):
                if 0 <= i+d[_][0] < N and 0 <= j+d[_][1] < N:
                    tmp += N_list[i+d[_][0]][j+d[_][1]]

            if tmp > max_value:
                max_idx = [i,j]
                max_value = tmp


    print(f'#{t} {" ".join(str(x) for x in max_idx+[max_value])}')
