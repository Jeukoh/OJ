T = int(input())
for t in range(1,T+1):
    a = input()
    b = input()

    Dict = {}
    #초기화
    for i in a:
        Dict[i] = 0

    anw = 0

    for i in b:
        if Dict.get(i) != None:
            Dict[i] += 1
            anw = anw if Dict[i] < anw else Dict[i]

    print(f'#{t} {anw}')