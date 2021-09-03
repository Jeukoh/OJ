import sys; readline=sys.stdin.read
N = int(input())
sticks = list(map(int,readline().split()))

cnt = 1
tmp = sticks[-1]
while sticks:
    value = sticks.pop(-1)
    if value > tmp:
       cnt += 1
       tmp = value

print(cnt)