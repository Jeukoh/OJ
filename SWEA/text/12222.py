def cals(t):
    stack = [t[0]]
    cur = 1
    while cur < len(t):
        if stack[-1] != t[cur]:
            stack.append(t[cur])
        else:
            tmp = t[cur]
            while stack[-1] == tmp:
                try:
                    cur += 1
                    tmp += t[cur]
                except:
                    stack.pop()
            stack.append(tmp)
        cur += 1
    return stack


for tc in range(1,int(input())+1):
    t = input()

    a=cals(t)
    print(f'#{tc} {len(a)}')
