def merge_sort(arr):
    def sort(l,r):
        global anw
        if r-l == 1:
            return arr[l:r]
        mid = (l+r)//2
        larr = sort(l,mid)
        rarr = sort(mid,r)
        if larr[-1] > rarr[-1]:
            anw += 1
        return merge(larr,rarr)
    def merge(larr,rarr):
        ret = []
        i = j = 0
        while i <len(larr) or j < len(rarr):
            if i <len(larr) and j < len(rarr):
                if larr[i] <= rarr[j]:
                    ret.append(larr[i])
                    i += 1
                else:
                    ret.append(rarr[j])
                    j += 1
            elif i < len(larr):
                ret.append(larr[i])
                i += 1
            else:
                ret.append(rarr[j])
                j += 1
        return ret
    return sort(0,len(arr))

for tc in range(1,int(input())+1):
    N = int(input())
    arr = list(map(int,input().split()))
    anw = 0
    arr_sort = merge_sort(arr)
    print(f'#{tc}', arr_sort[N//2], anw)