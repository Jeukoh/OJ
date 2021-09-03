const = 1000000
def bfs(N,M):
    stack = [N]
    f = -1
    r = 0
    visitdict = {N: 1}

    while r!=f:
        f += 1
        S = stack[f]
        if not visitdict.get(S+1) and S+1 <= const:
            visitdict[S+1] = visitdict[S]+1
            stack.append(S+1)
            r += 1
        if not visitdict.get(S-1) and 1 <= S-1 <= const:
            visitdict[S-1] = visitdict[S]+1
            stack.append(S-1)
            r += 1
        if not visitdict.get(2*S) and 2*S <= const:
            visitdict[2*S] = visitdict[S]+1
            stack.append(2*S)
            r += 1
        if not visitdict.get(S-10) and 1 <= S-10 <= const:
            visitdict[S-10] = visitdict[S]+1
            stack.append(S-10)
            r += 1
        if visitdict.get(M):
            return visitdict[M]



for tc in range(1,int(input())+1):
    N, M = map(int,input().split())
    print(f'#{tc}', bfs(N,M)-1)
