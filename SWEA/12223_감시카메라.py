from itertools import combinations
from math import comb

def makebox(camera1,camera2):
    x1,y1,x2,y2 = list(zip(camera1,camera2))
    nx1 = max(x1)
    ny1 = max(y1)
    nx2 = min(x2)
    ny2 = min(y2)

    #print(x1,y1,x2,y2)
    #print(nx1,ny1,nx2,ny2)

    if nx1 <= nx2 and ny1 <= ny2:
        return [nx1,ny1,nx2,ny2]
    else:
        return [-1,-1,-1,-1]

T = int(input())
for t in range(1,T+1):
    N = int(input())
    cameras = [list(map(int,input().split())) for _ in range(N)]
    # x1,y1,x2,y2

    cnt = 0
    print(cameras)
    cameras.sort(key= lambda x: (x[0],x[1]))
    print(cameras)
    max_box = cameras[0]
    for i in cameras:
        max_box = makebox(max_box,i)
        print(max_box)

    print(f'#{t} {cnt}')

