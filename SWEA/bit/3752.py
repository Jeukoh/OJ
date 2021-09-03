for tc in range(1,int(input())+1):
    N = int(input())
    score = list(map(int,input().split()))

    dict_score = {0:1}

    stack = [0]
    cnt = 0
    for i in score:
        for j in range(len(stack)):
            cnt += 1
            if dict_score.get(stack[j]+i):
                continue
            stack.append(stack[j]+i)
            dict_score[stack[j]+i] = 1




    print(f'#{tc}', len(dict_score))
    print(cnt)