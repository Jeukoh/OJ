def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return None

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        #print(f'low {low} high {high} pivot_idx {(low+high)//2}')
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1

        #print(arr)
        return low

    return sort(0, len(arr) - 1)



arr = [1,2,3,10,0,9,8,7] + [1,2,3,10,0,9,8,7]
print(arr)
quick_sort(arr)
print(arr)



# T = int(input())
# for _ in range(T):
#     N = int(input())
#     N_list = list(map(int,input().split()))
#
#     quick_sort(N_list)
#
#     print(f'#{_} {" ".join(str(x) for x in N_list)}')