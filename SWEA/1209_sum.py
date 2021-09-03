T = 10
for t in range(1,T+1):
    num_list = []
    int(input())
    for _ in range(100):
        num_list.append(list(map(int,input().split())))
    sum_row = [0]*100
    sum_column = [0]*100
    sum_dia = [0]*2
    max = 0
    for i in range(100):
        for j in range(100):
            sum_row[i] += num_list[i][j]
            sum_column[j] += num_list[i][j]
            if i==j:
                sum_dia[0] += num_list[i][j]
            if (i+j)==99:
                sum_dia[1] += num_list[i][j]


    for i in range(100):
        if max < sum_row[i]:
            max = sum_row[i]
        if max < sum_column[i]:
            max = sum_column[i]

    max = sum_dia[0] if sum_dia[0] > max else max
    max = sum_dia[1] if sum_dia[1] > max else max

    print(f'#{t} {max}')