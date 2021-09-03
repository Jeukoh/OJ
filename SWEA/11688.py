T = int(input())
i_list = []
for tc in range(1,T+1):
    text = input()
    a = b = 1

    for i in text:
        if i == 'L':
            b = a+b
        else:
            a = a+b

    print(f'#{tc}',a,b)