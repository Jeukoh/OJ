import sys; readline = sys.stdin.readline
from collections import deque

N, M = map(int,readline().split())
ladder = {}
for _ in range(N):
    x, y = map(int,readline().split())
    ladder[x] = y
snake = {}
for _ in range(M):
    x, y = map(int, readline().split())
    snake[x] = y

def bfs():
    dp = [-1] * 101
    Q = deque([1])
    dp[1] = 0
    while Q and dp[-1] == -1:
        x = Q.popleft()
        for _ in range(6,0,-1):
            nx = x+_
            if nx <= 100 and dp[nx] == -1:
                dp[nx] = dp[x] + 1
                if ladder.get(nx) and dp[ladder[nx]] == -1:
                    dp[ladder[nx]] = dp[x] + 1
                    Q.append(ladder[nx])
                elif snake.get(nx) and dp[snake[nx]] == -1:
                    dp[snake[nx]] = dp[x] + 1
                    Q.append(snake[nx])
                else:
                    if not ladder.get(nx) and not snake.get(nx):
                        Q.append(nx)
    return dp[-1]

print(bfs())