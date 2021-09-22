import sys; readline = sys.stdin.readline
from collections import deque
N, M = map(int,readline().split())
truthnum, *truth = map(int,readline().split())
party_node = [[] for _ in range(M+1)]
connected_party = [[] for _ in range(N+1)]
for idx in range(M):
    partynum, *partymember = map(int,readline().split())
    party_node[idx+1].extend(partymember)
    for i in partymember:
        connected_party[i].append(idx+1)
visited_party = [True]*(M+1)
visited_man = [True]*(N+1)

# put the man to truth
Q = deque(truth)
while Q:
    tman = Q.popleft()
    visited_man[tman] = False


    for party in connected_party[tman]:
        if visited_party[party]:
            visited_party[party] = False
            for man in party_node[party]:
                if visited_man[man]:
                    Q.append(man)

print(sum(visited_party)-1)
