import sys; read = sys.stdin.read
N = int(input())

a = list(map(int,read().split()))
anw = 0
max_v = a[-1]-1
for idx in range(N-2,-1,-1):

    max_v = a[idx+1]-1
    if a[idx] > max_v:
        anw += a[idx]-max_v
        a[idx] = max_v

print(anw)