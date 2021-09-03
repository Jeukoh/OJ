from bisect import bisect_left

N=int(input())
l = [int(input()) for _ in range(N)]
LIS = [l[0]]
root = [i-1 for i in range(N)]
root[0] = 0
for idx, v in enumerate(l):
    if not idx:
        continue
    if v > LIS[-1]:
        root[idx] = LIS[-1]
        LIS.append(v)
    else:
        x = bisect_left(LIS,v)
        LIS[x] = v
        root[idx] = LIS[x-1]


print(l)
print(N-len(LIS))
print(LIS)

anw = []

s_v = LIS[-1]
s_i = bisect_left(l,s_v)
anw.append(s_v)
while s_v != 0:
    s_v = root[s_i]
    s_i = bisect_left(l,s_v)
    anw.append(s_v)

print(list(reversed(anw))[1:])