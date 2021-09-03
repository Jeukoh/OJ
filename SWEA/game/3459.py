for tc in range(1,int(input())+1):
    N = int(input())

    flag = -1
    N//=2
    N+= 1
    while N > 1:
        if flag == -1:
            N//=2
        else:
            N = (N+1)//2

        flag *= -1

    anw = 'Bob' if flag == -1 else 'Alice'
    print(f'#{tc} {anw}')

cnta =0
cntb =0
for i in range(1,1001):
    N = i
    flag = -1
    N//=2
    N+= 1
    while N > 1:
        if flag == -1:
            N//=2
        else:
            N = (N+1)//2

        flag *= -1

    anw = 'Bob' if flag == -1 else 'Alice'
    if flag == 1:
        cnta +=1
    else:
        cntb += 1

print(cnta,cntb)