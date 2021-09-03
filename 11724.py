import sys; readline=sys.stdin.readline


N, M = map(int,readline().split())

map_dict = { i:[] for i in range(1,N+1)}
bool_list = [True]*N

for _ in range(M):
    a, b = map(int,readline().split())
    map_dict[a].append(b)
    map_dict[b].append(a)

def bfs(i):
    try:
        stack = [map_dict[i].pop()]
    except IndexError:
        bool_list[i-1] = False
        return None
    while stack:
        tmp= stack.pop()
        if bool_list[tmp-1]:
            bool_list[tmp - 1] = False
            stack.extend(map_dict[tmp])
            map_dict[tmp] = []
    return None

cnt = 0
for i in range(1,N+1):
    if bool_list[i-1]:
        cnt += 1
        bool_list[i-1] = False
        bfs(i)


print(cnt)