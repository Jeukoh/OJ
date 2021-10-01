def getPermutation(arr, start, end , n):
    if start == end:
        permu_set.add((''.join(arr),n))
    else:
        for i in range(start,end):
            nn = n
            if not arr[start] == arr[i]:
                nn += 1
            arr[start], arr[i] = arr[i], arr[start]
            getPermutation(arr,start+1,end,nn)
            arr[start], arr[i] = arr[i], arr[start]

for tc in range(1,int(input())+1):
    N, M = map(int,input().split())
    arr = list(str(N))
    permu_set = set()
    tmp_list = []
    getPermutation(arr, 0, len(arr),0)
    sameBool = False
    if len(set(arr)) != len(arr):
        sameBool = True
    arr = list(str(N))
    permu_set = sorted(list(permu_set))
    while permu_set:
        c, k = permu_set.pop()
        if M == k:
            anw = int(c)
            break
        elif M > k:
            if sameBool or not (M-k)%2:
                anw = int(c)
                break

    print(f'#{tc} {anw}')