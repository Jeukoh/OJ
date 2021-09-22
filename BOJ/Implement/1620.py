import sys; readline = sys.stdin.readline
N, M = map(int,readline().split())
numtoname = {}
nametonum = {}

for idx in range(1,N+1):
    name = readline().rstrip()
    numtoname[idx] = name
    nametonum[name] = idx
ret = []
for _ in range(M):
    query = readline().rstrip()
    if query.isalpha():
        ret.append(nametonum[query])
    else:
        ret.append(numtoname[int(query)])

print('\n'.join(map(str,ret)))