import sys; readline = sys.stdin.readline

N = int(input())
Arr = list(map(int,readline().split()))
stack = [Arr[-1]]
sol = [-1]*N
for i in range(len(Arr)-1,-1,-1):
    while stack:
        if Arr[i] < stack[-1]:
            sol[i] = stack[-1]
            break
        else:
            stack.pop(-1)
    stack.append(Arr[i])

print(' '.join(str(i) for i in sol))