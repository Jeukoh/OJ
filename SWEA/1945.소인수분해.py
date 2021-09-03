T = int(input())
for _ in range(T):
    N = int(input())

    count_list = [0]*5

    a = [2,3,5,7,11]

    for i in range(5):
        while not N%a[i]:
            count_list[i] += 1
            N //= a[i]

    print(f'#{_+1} {" ".join(str(x) for x in count_list)}')