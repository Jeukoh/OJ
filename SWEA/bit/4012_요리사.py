_comb = [[-1]*9 for _ in range(17)]
def comb(N,r):
    if _comb[N][r] != -1:
        return _comb[N][r]
    if N == r:
        return 1
    if N < r:
        return 0
    if r == 0:
        return 1
    _comb[N][r] = comb(N-1,r)+comb(N-1,r-1)
    return _comb[N][r]

def combinations(arr,r):
    pool = tuple(arr)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i+n-r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1,r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

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
    lim = comb(N,N//2)//2
    for A in combinations(range(N),N//2):
        B = set(range(N))-set(A)
        B = tuple(B)
        SA = calcS(A)
        SB = calcS(B)
        min_anw = min(min_anw,abs(SA-SB))
        cnt += 1
        if cnt == lim:
            break
    print(f'#{tc}', min_anw)