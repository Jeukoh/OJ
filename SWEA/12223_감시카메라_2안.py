import math

def countbit(n):
    cnt = 0
    while n>0:
        n &= n-1
        cnt +=1
    return cnt

T = int(input())
for t in range(1,T+1):
    N = int(input())
    cameras = [list(map(int,input().split())) for _ in range(N)]
    # x1,y1,x2,y2




    cnt = 0

    Map =[[0]*1000 for _ in range(1000)]

    for idx,camera in enumerate(cameras):
        for x in range(camera[0]-1,camera[2]):
            for y in range(camera[1]-1,camera[3]):
                Map[x][y] += 1<<(idx)

    case_v = set()

    for x in range(1000):
        for y in range(1000):
            case_v.add(Map[x][y])

    case_c = []

    for i in case_v:
        if countbit(i) >= 3:
            for j in case_v:
                if i != j and j&i == i:
                    break
            else:
                case_c.append(i)


    for i in case_c:
        print(bin(i))
        cnt += math.comb(countbit(i),3)

    print(f'#{t} {cnt}')

