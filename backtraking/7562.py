import sys; readline = sys.stdin.readline
from collections import deque

move = [[2,1],[1,2],[-2,1],[-1,2],[1,-2],[2,-1],[-1,-2],[-2,-1]]

tc = int(readline())

def bfs(Sx,Sy,Fx,Fy,L):
    visited = {}

    Q = deque([[Sx,Sy]])
    visited[(Sx,Sy)] = 1
    while Q:
        x,y = Q.popleft()
        for _ in range(8):
            nx, ny = x+move[_][0], y+move[_][1]
            if L>nx>=0 and L>ny>=0 and not visited.get((nx,ny)):
                visited[(nx,ny)] = visited[(x,y)] + 1
                Q.append([nx,ny])
                if nx == Fx and ny == Fy:
                    return visited[(nx,ny)] -1
    return 0
for _ in range(tc):
    L = int(input())
    Sx,Sy = map(int,input().split())
    Fx,Fy = map(int,input().split())
    print(bfs(Sx,Sy,Fx,Fy,L))