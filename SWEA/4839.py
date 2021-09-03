T = int(input())

def search(P,key):
    cnt = 0
    start = 1
    end = P
    while start <= end:
        cnt += 1
        mid = (start+end)//2
        if mid == key:
            return cnt
        elif key > mid:
            start = mid
        else:
            end = mid
    return cnt

for t in range(1,1+T):
    P, Pa, Pb = map(int,input().split())

    A = search(P,Pa)
    B = search(P,Pb)
    anw = 'A' if A < B else 'B' if B < A else '0'

    print(f'#{t} {anw}')