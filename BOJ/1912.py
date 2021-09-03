import sys; readline = sys.stdin.readline
N = int(input())
arr = list(map(int,readline().split()))
dp = arr[:]
max = max(arr)

for idx,v in enumerate(arr):
    if idx == 0:
        continue
    if dp[idx-1]+v > v:
        dp[idx] = dp[idx-1]+v
        if dp[idx] > max:
            max = dp[idx]


print(max)

