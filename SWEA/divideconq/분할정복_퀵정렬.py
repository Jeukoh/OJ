def quick_sort(arr):

    def sort(low,high):
        piv = arr[(low+high)//2]
        while low <= high:
            while arr[low] < piv:
                low += 1
            while arr[high] > piv:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low += 1
                high -= 1
        return low

    def partition(low,high):
        if low >= high:
            return
        mid = sort(low,high)
        partition(low,mid-1)
        partition(mid,high)
    return partition(0,len(arr)-1)

for tc in range(1,int(input())+1):
    N = int(input())
    arr = list(map(int,input().split()))
    quick_sort(arr)
    print(f'#{tc}', arr[N//2])