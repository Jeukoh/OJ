import sys; readline = sys.stdin.readline
sys.setrecursionlimit(10000000)

V = int(readline())
linked_list = [[] for _ in range(V+1)]
value_list = [[] for _ in range(V+1)]
value_sum = [0]*(V+1)

for _ in range(V):
    tmp = list(map(int,readline().split()))
    linked_list[tmp[0]]=(tmp[1:-1:2])
    value_list[tmp[0]]=(tmp[2::2])

def dfs(start,first_start):
    for idx, next in enumerate(linked_list[start]):
        if value_sum[next] == 0 and next != first_start:
            value_sum[next] = value_sum[start]+value_list[start][idx]
            dfs(next,first_start)

dfs(1,1)
max_value = 0
max_idx = 0
for idx, value in enumerate(value_sum):
    if value > max_value:
        max_value = value
        max_idx = idx
value_sum = [0]*(V+1)
dfs(max_idx,max_idx)
print(max(max(value_sum),max_value))
