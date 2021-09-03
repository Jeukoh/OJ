dx = [-1,0,1,0]
dy = [0,-1,0,1]
N, Pe, Pw, Ps, Pn = map(int,input().split())
Pe,Pw,Ps,Pn = map(lambda x: x*0.01,[Pe,Pw,Ps,Pn])
Pmap = {0:Pn,1:Pw,2:Ps,3:Pe}
anw = 0
visited = [[0]*(31) for _ in range(31)]

def dfs(x,y,k,anw_g):
    global anw
    if visited[x][y]:
        anw += anw_g
        return

    if k == N:
        return

    for _ in range(4):
        if Pmap[_]:
            nx, ny = x+dx[_], y+dy[_]
            visited[x][y] = True
            dfs(nx,ny,k+1,anw_g*Pmap[_])
            visited[x][y] = False


dfs(15,15,0,1)

print(1-anw)
