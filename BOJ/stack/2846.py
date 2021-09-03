import sys; readline=sys.stdin.readline
N= int(input())
i_l = list(map(int,readline().split()))

anw, s, e = 0, i_l[0], 0
for i in i_l:
    if i > e:
        e = i
    else:
        anw = max(anw,e-s)
        s = i
        e = i
anw = max(anw,e-s)
print(anw)