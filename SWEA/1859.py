T = int(input())

for _ in range(T):
    N = int(input())
    a_list = list(map(int,input().split()))

    stack = []
    anw = 0

    max_v = 0
    for idx,value in enumerate(reversed(a_list)):
        if value >= max_v:
            max_v = value
        else:
            anw += max_v-value


    print(f'#{_+1} {anw}')
