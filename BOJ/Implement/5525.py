import sys; readline = sys.stdin.readline
import re

N = int(input())
M = int(input())
S = input().strip()

cur = 1

cnt = 0
NP = 0
while cur < M-1:
    if S[cur-1] == 'I' and S[cur] == 'O' and S[cur+1] == 'I':
        NP += 1
        if NP == N:
            cnt += 1
            NP -= 1
        cur += 1
    else:
        NP = 0
    cur += 1

print(cnt)

''':var

import sys; readline = sys.stdin.readline
import re

N = int(input())
_ = input()
S = input().strip()
finds = 'O'.join(['I']*(N+1))
x = re.finditer(f'(?=({finds}))',S)
cnt = 0
for v in x:
    cnt += 1
print(cnt)

'''