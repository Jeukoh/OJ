import sys; readline = sys.stdin.readline
from itertools import combinations

inparr = []
while True:
    tmp = list(map(int,readline().split()))
    if tmp:
        inparr.append(tmp)
    else:
        break

for _ in range(len(inparr)-1):
    arr = inparr[_][1:]
    com = combinations(arr, 6)
    for i in com:
        print(' '.join(str(x) for x in i))

    print('')


