while True:
    try:
        tc = int(input())
        q = list(map(int,input().split()))
        r = len(q)-1
        i = 1
        while q[r] > 0:
            r = (r+1)%8
            q[r] -= i
            i = i%5+1
        q[r] = 0
        anw = ''
        for _ in range(1,9):
            anw = anw + str(q[(r+_)%8])
        print(f'#{tc}', ' '.join(anw))
    except EOFError:
        break
