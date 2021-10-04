import math

N = int(input())
K = [0,0,0]
tmp = list(map(int,input().split()))
dp = [[[0]*61 for __ in range(61)] for _ in range(61)]

for _ in range(N):
    K[_] = tmp[_]

def sol(N,K):
    if N == 1:
        return math.ceil(K[0]/9)

    min_cnt = 500
    def recur(s1,s2,s3,n):
        nonlocal min_cnt
        if s1 <= 0 and s2 <= 0 and s3 <= 0:
            min_cnt = min(min_cnt, n)
            return

        s1, s2, s3 = map(lambda x: max(0,x), [s1,s2,s3])

        if dp[s1][s2][s3] != 0 and dp[s1][s2][s3] <= n:
            return

        dp[s1][s2][s3] = n

        recur(s1-9,s2-3,s3-1,n+1)
        recur(s1 - 9, s2 - 1, s3 - 3, n + 1)
        recur(s1 - 3, s2 - 9, s3 - 1, n + 1)
        recur(s1 - 1, s2 - 9, s3 - 3, n + 1)
        recur(s1 - 1, s2 - 3, s3 - 9, n + 1)
        recur(s1 - 3, s2 - 1, s3 - 9, n + 1)

    recur(*K,0)
    return min_cnt

print(sol(N,K))

