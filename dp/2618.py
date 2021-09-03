import sys; readline = sys.stdin.readline
sys.setrecursionlimit(1000000)
def getmin(x,y):
    mission = max(x,y)+1
    if mission == W+1:
        return 0
    if dp[x][y] != -1: return dp[x][y]
    x_loc = A if x == 0 else events[x]
    y_loc = B if y == 0 else events[y]
    # x,y 에서 다음 미션을 위해 x가 움직이는 경우는 거리는
    move_x = getmin(mission,y) + dist(x_loc,events[mission])
    move_y = getmin(x,mission) + dist(y_loc,events[mission])
    ret = min(move_x,move_y)
    dp[x][y] = ret
    return ret

def dist(x,y):
    return abs(x[0]-y[0])+abs(x[1]-y[1])


def traceget(x,y):
    mission = max(x, y) + 1
    if mission == W + 1:
        return 0
    x_loc = A if x == 0 else events[x]
    y_loc = B if y == 0 else events[y]
    # x,y 에서 다음 미션을 위해 x가 움직이는 경우는 거리는
    move_x = getmin(mission, y) + dist(x_loc, events[mission])
    move_y = getmin(x, mission) + dist(y_loc, events[mission])

    if move_x < move_y:
        trace[mission] = 1
        traceget(mission,y)
    else:
        trace[mission] = 2
        traceget(x,mission)


N = int(input())
W = int(input())
events = [()]
for _ in range(W):
    events.append(tuple(map(int,input().split())))
dp = [[-1]*(W+1) for _ in range(W+1)]
trace = {}
#dp[x][y] A의 마지막미션이 x이고 B의 마지막 미션이 y일때 max(x+y)+1 사건을 해결하기 위한 이동거리 중 거리 최소,
A = (1,1)
B = (N,N)
getmin(0,0)
traceget(0,0)
print(dp[0][0])
print('\n'.join(str(trace[i]) for i in range(1,W+1)))