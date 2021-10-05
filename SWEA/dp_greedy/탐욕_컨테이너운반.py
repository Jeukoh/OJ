def quicksort(arr):
    def part(l,r):
        piv = arr[(l+r)//2]
        while l <= r:
            while piv > arr[l]:
                l += 1
            while piv < arr[r]:
                r -= 1
            if l <= r:
                arr[l], arr[r] = arr[r], arr[l]
                r -= 1
                l += 1
        return l

    def sort(l,r):
        if r <= l:
            return
        mid = part(l,r)
        sort(l,mid-1)
        sort(mid,r)

    return sort(0,len(arr)-1)

for tc in range(1,int(input())+1):
    N, M = map(int,input().split())
    ws = list(map(int,input().split()))
    ts = list(map(int,input().split()))
    anw = 0
    quicksort(ws)
    quicksort(ts)
    while ts and ws:
        truck = ts.pop()
        weight = ws.pop()
        while ws and weight > truck:
            weight = ws.pop()
        if truck >= weight:
            anw += weight
    print(f'#{tc}', anw)