import sys; readline = sys.stdin.readline
N = int(input())
heights = list(map(int,readline().split()))

# 보이는지 안보이는지 bool 리턴
def bool_building(x1,x2):
    if x2-x1 == 1:
        return True
    else:
        slope = (heights[x2]-heights[x1])/(x2-x1)
        for i in range(x1+1,x2):
            if slope*(i-x1)+heights[x1] <= heights[i]:
                return False
        return True

cnt = [0]*N

for x1 in range(0,N-1):
    for x2 in range(x1+1,N):
        if bool_building(x1,x2):
            cnt[x1] += 1
            cnt[x2] += 1


print(max(cnt))