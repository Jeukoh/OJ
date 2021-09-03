T = int(input())
for _ in range(T):
    N = int(input())
    a_list = list(map(int,input().split()))

    anw = -600

    for idx in range(len(a_list)-1):
        tmp = a_list[idx] + a_list[idx+1]

        anw = anw if anw>tmp else tmp

    print(f'#{_+1} {anw}')

