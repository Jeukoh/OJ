T = int(input())

for t in range(1,T+1):

    alpha, N = input().split()
    N = int(N)
    len_alpha = len(alpha)

    flag = True
    possible_case = [1]
    case_sum = 0
    while flag:

        possible_case.append(len_alpha**(len(possible_case)))
        case_sum += possible_case[-1]
        if case_sum >= N:
            flag = False


    N_case = N - sum(possible_case[:-1])

    corsor = len(possible_case)-2
    anw = ''

    while corsor >= 0:
        anw += alpha[N_case//possible_case[corsor]]
        N_case %= possible_case[corsor]
        corsor -= 1

    print(f'#{t} {anw}')