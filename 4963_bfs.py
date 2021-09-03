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

def bfs(x,y): # 가까운거 다 돌면서 0으로 만들고 더이상 추가되는 stack이 없을때 나오기
    stack = [[x,y]]
    tmp = []
    while stack:
        for n,i in enumerate(stack): # stack에는 방문해야할 다음 섬들의 위치가 담겨있다
            x = i[0]
            y = i[1]
            for _ in range(8):
                newx = x+dx[_]
                newy = y+dy[_]
                if 0<=newx<w and 0<=newy<h and MP[newy][newx]:
                    tmp.append([newx,newy])
                    MP[newy][newx] = 0
        stack = tmp
        tmp = []
    return 1

while True:
    w,h = map(int,readline().split())
    if w == 0 and h == 0:
        break
    MP = []
    numI = 0

    for j in range(h):
        a=list(map(int, readline().split()))
        MP.append(a)


    visited = []
    for x in range(w):
        for y in range(h):
            if MP[y][x]:
                MP[y][x] = 0
                numI += bfs(x,y)

    print(f'{numI}')


