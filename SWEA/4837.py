T = int(input())

def countbit(number):
    count = 0
    while number > 0:
        number = number&(number-1)
        count += 1
    return count


for t in range(1,1+T):
    N_list = [i for i in range(1,13)]
    N, K = map(int,input().split())


    count = 0

    for i in range(1<<12): # 모든 부분집합의 수 mask 2^12-1개
        if countbit(i) == N:
            pasum = 0
            for j in range(12):
                if i & (1<<j):
                    pasum += N_list[j]

            if pasum == K:
                count += 1

    print(f'#{t} {count}')