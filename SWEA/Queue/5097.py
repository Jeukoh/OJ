dx = (-1,0,1,0)
dy = (0,-1,0,1)
def bfs():
    global stack
    anw = 0
    while stack:
        tmp_stack = []
        for x,y in stack:
            for _ in range(4):
                nx, ny = x + dx[_], y + dy[_]
                if N>nx>=0 and N>ny>=0 and Map[nx][ny] != 1:
                    if Map[nx][ny] == 3:
                        return anw
                    tmp_stack.append([nx,ny])
                    Map[nx][ny] = 1
        stack = tmp_stack[:]
        anw += 1
    return 0
for tc in range(1,int(input())+1):
    N = int(input())
    Map = []
    stack = []
    for _ in range(N):
        tmp = list(map(int, input()))
        Map.append(tmp)
        if 2 in tmp:
            stack.append([_,tmp.index(2)])

    Map[stack[0][0]][stack[0][1]] = 1

    print(f'#{tc} {bfs()}')
