tc = int(input())
k = 100
out = [0]*k
flag = False
for _ in range(tc//k):
    for x in range(k):
        try:
            A,B,C,D = map(int,input().split())
        except:
            print('\n'.join(f'#{k*_+i+1} {out[i]}' for i in range(x)))
            flag = True
            break

        s = max(A,C)
        e = min(B,D)
        out[x] = max(0,e-s)

    if flag:
        break
    else:
        print('\n'.join(f'#{k*_+i+1} {out[i]}' for i in range(k)))

