for tc in range(1, int(input())+1):
    b = float(input().strip())
    cnt = 0
    while b != int(b):
        b *= 2
        cnt += 1
        if cnt >= 13:
            break
    if cnt == 13:
        ret = 'overflow'
    else:
        ret = bin(int(b))[2:].zfill(cnt)
    print(f'#{tc}', ret)
