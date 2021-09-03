import sys

def findv(r,c): # 가장 가까운 코너의 좌표를 찾아 좌표의 값을 리턴해줌
    shidx = max(abs(r),abs(c))
    #오른쪽 아래 값은 (2*shidx+1)^2 좌표는 (shidx,shidx)
    shval = (2*shidx+1)**2
    corner = [shval, shval-2*shidx,shval-4*shidx,shval-6*shidx] #오른쪽아래, 왼쪽 아래, 왼쪽 위, 오른쪽 위의 값
    #4가지 경우
    if r==shidx:
        return corner[0] - (shidx-c)
    elif c==-1*shidx:
        return corner[1]-(shidx-r)
    elif r==-1*shidx:
        return corner[2] - (c+shidx)
    else:
        return corner[3] - (r+shidx)

readr = sys.stdin.readline
r1,c1,r2,c2 = list(map(int,readr().split()))
cl,rl =c2-c1+1, r2-r1+1
prlist = {}
for r in range(r1,r2+1):
    for c in range(c1,c2+1):
        prlist[(r,c)] = findv(r,c)
numc = len(str(max(prlist.values())))
for x in range(r1,r2+1):
    for y in range(c1,c2+1):
        print("{0:{1}d}".format(prlist[(x,y)],numc),end=' ')
    print()




