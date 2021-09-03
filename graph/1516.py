import sys; readline = sys.stdin.readline

class Node:
    def __init__(self,time,root):
        self.time = time
        self.root = root
        self.min_time = 0

def recurmin_time(i):
    if tree[i].min_time:
        return tree[i].min_time
    tmp = 0
    for x in tree[i].root:
        tmp = max(tmp,recurmin_time(x))
    tree[i].min_time = tree[i].time + tmp
    return tree[i].min_time

N = int(input())
tree = [0]*(N+1)
for _ in range(N):
    tmp = list(map(int,readline().split()))[:-1]
    tree[_+1] = Node(tmp[0],tmp[1:])
for i in range(1,N+1):
    print(recurmin_time(i))

