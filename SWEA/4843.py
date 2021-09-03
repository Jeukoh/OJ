T = int(input())

def quicksort(arr):
    def part(low,high):
        pivot = arr[(low+high)//2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low += 1
                high -= 1
        return low

    def binary_search(low,high):
        if high <= low:
            return
        mid = part(low,high)
        binary_search(low,mid-1)
        binary_search(mid,high)

    return binary_search(0,len(arr)-1)


for t in range(1,1+T):
    N = int(input())
    N_list = list(map(int,input().split()))

    quicksort(N_list)

    anw_list = [0]*10

    for idx in range(10):
        if idx%2:
            anw_list[idx] = N_list[idx//2]
        else:
            anw_list[idx] = N_list[-1-idx//2]

    print(f'#{t} {" ".join(str(x) for x in anw_list)}')