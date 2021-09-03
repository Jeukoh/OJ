from collections import deque
for tc in range(1,int(input())+1):
    N = int(input())
    a = list(input().split())
    anw = []
    up = deque(a[:(len(a)+1)//2])
    down = deque(a[(len(a)+1)//2:])
    while up and down:
        anw.append(up.popleft())
        anw.append(down.popleft())
    if up:
        anw.append(up.popleft())
    print(f'#{tc} {" ".join(x for x in anw)}')