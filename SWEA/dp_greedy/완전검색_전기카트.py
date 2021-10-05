def rec(cur,i,ss):
    global min_anw

    if i == N-1:
        ss += adj_mat[cur-1][0]
        if ss < min_anw:
            min_anw = ss

    if ss >= min_anw:
        return

    if i == 0:
        for _ in range(2,N+1):
            if visited[_]:
                visited[_] = False
                rec(_,i+1,ss+adj_mat[0][_-1])
                visited[_] = True
    else:
        for _ in range(2,N+1):
            if visited[_]:
                visited[_] = False
                rec(_,i+1,ss+adj_mat[cur-1][_-1])
                visited[_] = True



for tc in range(1,int(input())+1):
    N = int(input())
    adj_mat = [list(map(int,input().split())) for _ in range(N)]
    min_anw = float('inf')
    visited = [True for _ in range(N+1)]

    rec(0,0,0)

    print(f'#{tc}', min_anw)