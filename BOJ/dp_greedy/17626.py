import sys; readline=sys.stdin.readline
from collections import deque
dp = [i**2 for i in range(int(50000**(1/2))+1)]
N = int(readline())
cnt = 0
def bfs(N):

    visited = {}
    Q = deque([N])
    visited[N] = 1

    while Q:

        n = Q.popleft()
        for x in range(int(n**(1/2))//2+1,int(n**(1/2))+1):
            if not visited.get(n-dp[x]):
                visited[(n-dp[x])] = visited[n]+1
                Q.append(n-dp[x])
                if n-dp[x] == 0:
                    return visited[0]

print(bfs(N)-1)
