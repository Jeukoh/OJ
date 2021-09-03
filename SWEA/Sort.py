def bubble(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [5,4,1,3,7,0]
bubble(arr)


def counting(arr):
    max_num = 10
    anw = [0]*len(arr)
    countsum = [0]*(max_num+1)
    for i in arr:
        countsum[i] += 1
    for idx in range(len(countsum)-1):
        countsum[idx+1] += countsum[idx]

    for idx in range(len(arr)-1,-1,-1):
        countsum[arr[idx]] -= 1
        anw[countsum[arr[idx]]] = arr[idx]
    return anw

arr = [5,4,1,3,7,7,0,0,10]
anw = counting(arr)


def selectingsort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i,len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [0,5,4,1,3,7,0]
selectingsort(arr)

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


def merge_sort(arr):
    def sort(low,high):
        #print('sort',low,high)
        if high-low <= 1:
            return arr[low:high]

        mid = (low+high)//2
        left_list = sort(low,mid)
        right_list = sort(mid,high)
        return merge(left_list,right_list)

    def merge(left,right):
        #print('merge',left, right)
        result = []
        i = 0
        j = 0
        while i < len(left) or j < len(right) :
            if i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            elif i < len(left):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        #print('result', result)
        return result
    return sort(0,len(arr))

arr = [1,2,3,10,0,9,8,7] + [1,2,3,10,0,9,8,7,3]
print(arr)
anw = merge_sort(arr)
print(anw)