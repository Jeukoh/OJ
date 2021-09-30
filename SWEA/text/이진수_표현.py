anw = []; tc = int(input())
for _ in range(tc):
    N, M = map(int,input().split())
    K = bin(M)[2:]
    if len(K) < N: anw.append('OFF')
    else:
        KK = K[-N:]
        if all(list(map(int,KK))): anw.append('ON')
        else: anw.append('OFF')
print('\n'.join(f'#{idx+1} {anw[idx]}' for idx in range(tc)))