for tc in range(1,int(input())+1):
    a = [input() for _ in range(5)]
    max_len = 0
    for i in a:
        max_len = len(i) if len(i) > max_len else max_len
    for idx, v in enumerate(a):
        a[idx] += '/'*(max_len-len(v))
    anw = ''
    for i in zip(*a):
        anw += ''.join(x for x in i)

    print(f'#{tc}', anw.replace('/',''))