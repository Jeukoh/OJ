from bisect import bisect_left
import sys; readline = sys.stdin.readline

T = int(readline())

for tc in range(T):
    N, M = map(int,readline().split())
    A = list(map(int,readline().split()))
    B = list(map(int,readline().split()))
    B.sort()

    anw = 0
    for i in A:
        x = bisect_left(B,i)
        anw += x
    print(anw)
