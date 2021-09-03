import math

def slope_y0(line):
    x1,y1,x2,y2 = line
    if x2 != x1:
        slope = (y2-y1)/(x2-x1)
        y0 = y1-slope*x1
    else:
        slope = math.inf
        y0 = x1
    return slope, y0

T = int(input())
for t in range(1,1+T):
    G, N = list(map(int,input().split()))
    slope_set = set()
    line_set = set()

    for _ in range(N):
        slope, y0 = slope_y0(list(map(int,input().split())))
        slope_set.add(slope)
        line_set.add((slope,y0))

    if len(slope_set) == 1:
        num_area = len(line_set)+1
    else:
        num_area = len(line_set)*2

    if num_area >= G:
        anw = 0
    else:
        anw= math.ceil(G/2)-len(line_set)

    # print(slope_set)
    # print(line_set)
    # print(num_area)
    print(f'#{t}', anw)