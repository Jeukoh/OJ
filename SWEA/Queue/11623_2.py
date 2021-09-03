
for tc in range(1,int(input())+1):
    q = [i+1 for i in range(int(input()))]

    cnt = len(q)
    cur = 0

    while cnt > 1:
        cnt -= 1
        q[cur] = -1
        while q[cur] == -1:
            cur = (cur+1)%len(q)
        cur = (cur+1)%len(q)
        while q[cur] == -1:
            cur = (cur+1)%len(q)

    for i in q:
        if i != -1:
            anw = i
            break

    print(f'#{tc}', anw)