def coor(n,a):
    if n == 0:
        return [0,0]
    k = 2**(2*(n-1))
    tmp_anw = [0,0]

    tmp_anw[0] += (a // k) // 2 * (k ** (1 / 2))
    if (a//k) == 1 or a//k == 2:
        tmp_anw[1] += (k**(1/2))

    y = coor(n-1,a%k)

    if a//k == 0:
        return [tmp_anw[0]+y[1],tmp_anw[1]+y[0]]
    elif a//k == 3:
        return [tmp_anw[0]+(k**(1/2)-1)-y[1],tmp_anw[1]+(k**(1/2)-1)-y[0]]
    else:
        return [tmp_anw[0]+y[0],tmp_anw[1]+y[1]]

def dis(a,b):
    return 10*((a[0]-b[0])**2 + (a[1]-b[1])**2)**(1/2)


T = int(input())
for t in range(1,1+T):
    n, a, b = map(int,input().split())

    a -= 1
    b -= 1

    coor_a = coor(n,a)
    coor_b = coor(n,b)

    print(f'#{t} {round(dis(coor_a,coor_b))}')
    print(coor_a,coor_b)



