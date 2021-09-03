import sys; readline = sys.stdin.readline
x = []
for _ in range(10):
    x.append(int(readline()))
anw = 0
plus, none = 0, 0
for idx in range(10):
    none = plus
    plus += x[idx]

    if abs(100-anw) >= abs(100-plus):
        anw = plus

print(anw)