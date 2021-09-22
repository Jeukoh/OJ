import sys; readline = sys.stdin.readline

R, C = map(int,readline().split())

Inf = -float('inf')

updp = []
dwdp = []
for _ in range(R):
    sub = list(map(int,readline().split()))
    updp.append([Inf]+sub[:])
    dwdp.append(sub[:]+[Inf])
updp.append([Inf]*(C+1))
dwdp.append([Inf]*(C+1))
for c in range(1,C+1):
    for r in range(R-1,-1,-1):
        if c == 1 and r == R-1:
            continue
        nc = C-c
        updp[r][c] += max(updp[r+1][c],updp[r][c-1])
        dwdp[r][nc] += max(dwdp[r+1][nc],dwdp[r][nc+1])


max_v = Inf
for r in range(R):
    for idx in range(C):
        tmp = updp[r][idx+1] + dwdp[r][idx]
        # print(r,idx,tmp)
        max_v = max(max_v,tmp)


# print(updp)
# print(dwdp)

print(max_v)