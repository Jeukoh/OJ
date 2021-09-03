import sys; readline = sys.stdin.readline

def retadj(i,j):
    for x in adj[i]:
        if x[0] == j:
            return x[1]

def Prim(S):
    visited = [True]*(V+1)
    root = [i for i in range(V+1)]
    MC = [maxi]*(V+1)
    MC[S] = -1*maxi

    for _ in range(V):
        min_v = maxi
        min_idx = -1
        for i in range(1,V+1):
            if visited[i] and MC[i] < min_v:
                min_v = MC[i]
                min_idx = i
        visited[min_idx] = False

        for value in adj[min_idx]:
            if visited[value[0]] and value[1] < MC[value[0]]:
                MC[value[0]] = value[1]
                root[value[0]] = min_idx

    anw = 0
    print(MC)
    for i in range(2,V+1):
        anw += retadj(i,root[i])
    return anw

maxi = 1000001
V, E = map(int,input().split())
adj = {i:[] for i in range(1,V+1)}
for _ in range(E):
    a,b,c = map(int,input().split())
    adj[a].append([b,c])
    adj[b].append([a,c])

root = Prim(1)
print(root)