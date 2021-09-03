from collections import deque

for tc in range(1,int(input())+1):
    q = deque([i+1 for i in range(int(input()))])

    while len(q) > 1:
        q.popleft()
        q.rotate(-1)

    print(f'#{tc}', q[0])