import sys; readline = sys.stdin.readline

N = int(readline())
weights = list(map(int,readline().split()))
TestN = int(readline())
Test_weights = list(map(int,readline().split()))

maxi=sum(weights)
dp = ['N']*(maxi+1)
dp[maxi] = 'Y'

stack = [sum(weights)]


for i in range(N):
    stack_tmp = stack[:]
    while stack_tmp:
        corsor = stack_tmp.pop()
        if dp[abs(corsor-weights[i])] == 'N':
            dp[abs(corsor - weights[i])] = 'Y'
            stack.append(abs(corsor-weights[i]))
        if dp[abs(corsor-2*weights[i])] == 'N':
            dp[abs(corsor - 2*weights[i])] = 'Y'
            stack.append(abs(corsor-2*weights[i]))

anw = []

for v in Test_weights:
    if v <= maxi:
        anw.append(dp[v])
    else:
        anw.append('N')

print(' '.join(str(x) for x in anw))
