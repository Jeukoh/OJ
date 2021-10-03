import sys; readline = sys.stdin.readline

def gcd(a,b):
    while b >= 1:
        a, b = b, a%b
    return a


def lcm(a,b):
    return (a*b)//gcd(a,b)



tc = int(readline())
anw = [0]*tc
for _ in range(tc):
    M,N,x,y = map(int,readline().split())

    x -= 1
    y -= 1
    p = 0

    lim = lcm(N,M)
    cand = 0
    while cand <= lim:
        cand = (M)*p + x
        ycal = cand%(N)
        #print(p,cand,ycal)
        if ycal == y:
            anw[_] = cand+1
            break
        p += 1

    if cand > lim:
        anw[_] = -1


print('\n'.join(str(x) for x in anw))