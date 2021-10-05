def chooseh(h,i):
    global anw
    if h >= 0:
        anw = min(anw,h)
        return
    if i == N:
        return
    chooseh(h+heights[i],i+1)
    chooseh(h, i + 1)

for tc in range(1,int(input())+1):
    N, K = map(int,input().split())
    heights = list(map(int,input().split()))
    heights.sort(reverse=True)
    anw = float('inf')
    chooseh(-K,0)
    print(f'#{tc}', anw)