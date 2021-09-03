import sys
sys.setrecursionlimit(10000000)
readline = sys.stdin.readline


dx = [+1, +1, +1, 0, -1, -1, -1, 0]
dy = [+1, 0, -1, -1, -1, 0, +1, +1]

"""
dfs()
1.아웃처리 조건 (노드의 끝 or 레인지 밖의 인풋)
2.노드에 도착하였을 때 행동 
ex ) count, visited, append ~
3. 다음 node로의 이동
for ~
dfs(new_x,new_y)
"""

"""
bfs()
1. 정의
queue = [root]
visit = []
temp = []
2. queue 돌기

for n,i in enumerate(queue):
    # 아웃처리 (queue에 채울때 해도 됨)
    
    #행동 -> temp queue에 채움 
    if x
"""
def dfs(x,y):
    if x < 0 or x >= w or y < 0 or y >= h:
        return None
    if MP[y][x] == 0 or boolmap[y][x] == False or [x,y] in visited:
        return None

    boolmap[y][x] = False
    visited.append([x,y])
    for _ in range(8):
        dfs(x+dx[_],y+dy[_])

    return None

while True:
    w,h = map(int,readline().split())
    if w == 0 and h == 0:
        break
    MP = []
    numI = 0
    boolmap = [[False]*w for _ in range(h)]

    for j in range(h):
        a=list(map(int, readline().split()))
        MP.append(a)

        for n,i in enumerate(a):
            if i == 1:
                boolmap[j][n] = True # n==x j == y x,y


    visited = []
    for x in range(w):
        for y in range(h):
            if MP[y][x] == 1 and not [x,y] in visited:
                numI += 1
                dfs(x,y)

    print(f'{numI}')


