import sys; readline = sys.stdin.readline
N = int(readline().rstrip())
budget = 0
cases = []
valid = True
for _ in range(N):
    a, b = map(int,readline().split())

    if budget+a < 0:
        cases.append([-1*a-budget,b-1*a-budget])
        budget = b
    else:
        if budget+a == b:
            budget = b
        else:
            valid = False
            break

def gdc(x,y):
    while y >= 1:
        x, y = y, x%y
    return x

if valid:
    if len(cases) >= 2:
        gdc_v = gdc(cases[0][1],cases[1][1])

        for idx in range(len(cases)):
            gdc_v = gdc(gdc_v,cases[idx][1])
            if gdc_v == 1:
                break

        for idx in range(len(cases)):
            if cases[idx][1] - gdc_v >= cases[idx][0]:
                gdc_v = -1
                break
    elif len(cases) == 1:
        gdc_v = cases[0][1]
    else:
        gdc_v = 1
else:
    gdc_v = -1

print(gdc_v)