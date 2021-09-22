import sys; readline = sys.stdin.readline
from collections import deque
N = int(readline().rstrip())
que = deque()
for _ in range(N):
    q = readline().split()
    try:
        if q[0] == 'push':
            que.append(int(q[1]))
        elif q[0] == 'pop':
            print(que.popleft())
        elif q[0] == 'size':
            print(len(que))
        elif q[0] == 'empty':
            if que:
                print(0)
            else:
                print(1)
        elif q[0] == 'front':
            print(que[0])
        else:
            print(que[-1])

    except:
        print(-1)