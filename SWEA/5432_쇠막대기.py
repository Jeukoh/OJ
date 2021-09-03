for tc in range(1,int(input())+1):
    a = input()
    cur = 0
    now = 0
    anw = 0
    while cur <= len(a)-2:
        if a[cur] == '(' and a[cur+1] == ')':
            anw += now
            cur += 1
        elif a[cur] == '(':
            now += 1
        elif a[cur] == ')':
            anw += 1
            now -= 1
        cur += 1
    print(f'#{tc} {anw+now}')