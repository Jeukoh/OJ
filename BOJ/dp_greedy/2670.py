import sys; read = sys.stdin.read
N = int(input())
arr = list(map(float,read().split()))
dp = arr[:]
Max = max(arr)

for idx,v in enumerate(arr):
    if idx == 0:
        continue
    if dp[idx-1]*v > v:
        dp[idx] = dp[idx-1]*v
        if dp[idx] > Max:
            Max = dp[idx]

print(f'{Max:.3f}')