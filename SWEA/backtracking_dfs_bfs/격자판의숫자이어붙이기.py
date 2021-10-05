dx = (-1,0,1,0)
dy = (0,-1,0,1)

def dfs(ans,x,y):

    if len(ans) == 7:
        pos_num_set.add(''.join(x for x in ans))
        return

    for _ in range(4):
        nx, ny = x+dx[_], y+dy[_]
        if 0 <= nx < 4 and 0 <= ny < 4:
            ans.append(Map[nx][ny])
            dfs(ans,nx,ny)
            ans.pop()

for tc in range(1,int(input())+1):
    Map = [input().split() for _ in range(4)]

    pos_num_set = set()

    for x in range(4):
        for y in range(4):
            dfs([],x,y)

    print(f'#{tc}', len(pos_num_set))