from itertools import combinations

# def combinations(arr,r):
#     pool = tuple(arr)
#     n = len(pool)
#     if r > n:
#         return
#     indices = list(range(r))
#     yield tuple(pool[i] for i in indices)
#     while True:
#         for i in reversed(range(r)):
#             if indices[i] != i+n-r:
#                 break
#         else:
#             return
#         indices[i] += 1
#         for j in range(i+1,r):
#             indices[j] = indices[j-1] + 1
#         yield tuple(pool[i] for i in indices)

def calcS(A):
    ret = 0
    for sub in combinations(A,2):
        ret += Stable[sub[0]][sub[1]]
        ret += Stable[sub[1]][sub[0]]
    return ret

for tc in range(1,int(input())+1):
    N = int(input())
    Stable = [list(map(int, input().split())) for _ in range(N)]
    min_anw = float('inf')
    cnt = 0
    visited = set()
    for A in combinations(range(N),N//2):
        if A in visited:
            break
        B = set(range(N))-set(A)
        B = tuple(B)
        visited.add(A)
        visited.add(B)
        SA = calcS(A)
        SB = calcS(B)
        min_anw = min(min_anw,abs(SA-SB))

    print(f'#{tc}', min_anw)