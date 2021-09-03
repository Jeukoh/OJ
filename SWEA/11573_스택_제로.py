for t in range(1,int(input())+1):
    stack = []
    input()
    num_list = list(map(int,(input().split())))

    for i in num_list:
        if i == 0:
            stack.pop()
        else:
            stack.append(i)


    print(f'#{t}',sum(stack))