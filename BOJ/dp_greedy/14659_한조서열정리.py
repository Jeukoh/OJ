N = int(input())
arr = list(map(int,input().split()))

anw = 0
max_v = arr[0]
cnt = 0
for v in arr:
    if v < max_v:
        cnt += 1
    else:
        max_v = v
        anw = max(anw, cnt)
        cnt = 0

print(max(anw, cnt))