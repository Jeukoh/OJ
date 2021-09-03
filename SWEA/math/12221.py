for tc in range(1,int(input())+1):
    A, B = map(int,input().split())
    if A >= 10 or B >= 10:
        anw = -1
    else:
        anw = A*B
    print(f'#{tc} {anw}')