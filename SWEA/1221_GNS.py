T = int(input())


hash_re = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
hash = {v:i for i, v in enumerate(hash_re)}


def quicksort(arr):
    def sort(low,high):
        if high <= low:
            return
        mid = partition(low,high)
        sort(low,mid-1)
        sort(mid,high)

    def partition(low,high):
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
    return sort(0,len(arr)-1)

for t in range(1,T+1):
    anw1, length = input().split()
    length = int(length)

    num_list = list(map(lambda x: hash[x], input().split()))


    quicksort(num_list)

    print(anw1)
    print(' '.join(hash_re[i] for i in num_list))
