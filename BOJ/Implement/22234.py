import sys; readline=sys.stdin.readline
#print = sys.stdout.write
from collections import deque

N, T, W = map(int,readline().split())
wait = deque()
for _ in range(N):
    wait.append(list(map(int,readline().split())))

M = int(readline())
# p,t,c id, time, 들어오는 시간 c
after = []
for _ in range(M):
    after.append(list(map(int,readline().split())))
after.sort(key = lambda x: -x[2])

anw = [0]*W
time = 0
tt = 0
while time < W:
    anw[time] = wait[0][0]
    wait[0][1] -= 1
    tt += 1
    time += 1
    if after and time == after[-1][2]:
        wait.append(after.pop()[:2])
    if tt == T or not wait[0][1]:
        if tt == T and wait[0][1]:
            wait.rotate(-1)
        else:
            wait.popleft()
        tt = 0

print('\n'.join(str(x) for x in anw))