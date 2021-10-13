d = ((1,1),(1,-1),(-1,-1),(-1,1))

def dfs(pos,i):
    global anw
    if i == 3 and stepcount[1] == stepcount[-1]:
        anw = max(anw,len(visited))
        return
    x, y = pos
    if i <= 1:
        nx, ny = x + d[i][0], y + d[i][1]
        if 0 <= nx < N and 0 <= ny < N and table[nx][ny] not in visited:
            visited.append(table[nx][ny])
            stepcount[i] += 1
            dfs((nx,ny),i)
            stepcount[i] -= 1
            visited.pop()
        nx, ny = x + d[i+1][0], y+ d[i+1][1]
        if stepcount[i] and 0 <= nx < N and 0 <= ny < N and table[nx][ny] not in visited:
            visited.append(table[nx][ny])
            stepcount[i+1] += 1
            dfs((nx,ny),i+1)
            stepcount[i + 1] -= 1
            visited.pop()
    else:
        if 2*(stepcount[0]+stepcount[1]) <= anw:
            return
        nx, ny = x + d[i][0], y + d[i][1]
        if 0 <= nx < N and 0 <= ny < N and stepcount[i] < stepcount[i-2] and table[nx][ny] not in visited:
            visited.append(table[nx][ny])
            stepcount[i] += 1
            dfs((nx,ny),i)
            stepcount[i] -= 1
            visited.pop()

        elif stepcount[i] == stepcount[i-2]:
            nx, ny = x + d[i+1][0], y + d[i+1][1]
            if table[nx][ny] not in visited:
                visited.append(table[nx][ny])
                stepcount[i+1] += 1
                dfs((nx, ny), i+1)
                stepcount[i+1] -= 1
                visited.pop()




for tc in range(1,int(input())+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    anw = -1
    visited = []
    stepcount = [0,0,0,0]
    for x in range(N-2):
        for y in range(N-1):
            dfs((x,y),0)

    print(f'#{tc}', anw)