tc = int(input())
k = 100
out = [0]*k
flag = False
for _ in range(tc//k):
    for idx in range(k):
        try:
            A,B = map(int,input().split())
        except:
            print('\n'.join(f'#{k*_+i+1} {out[i]}' for i in range(idx)))
            flag = True
            break

        x = B-A
        K = (x**2-x-2*A)//2

        out[idx] = K

    if flag:
        break
    else:
        print('\n'.join(f'#{k*_+i+1} {out[i]}' for i in range(k)))
