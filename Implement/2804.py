import sys; readline = sys.stdin.readline

a, b = readline().split()

for idx, value in enumerate(a):
    if value in b:
        a_idx = idx
        b_idx = b.index(value)
        break

Map = [['.']*len(a) for _ in range(len(b))]

for x in range(len(b)):
    for y in range(len(a)):
        if x == b_idx:
            Map[x] = list(a)

        if y == a_idx:
            Map[x][y] = b[x]


print('\n'.join(''.join(x for x in y) for y in Map))