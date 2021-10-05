def getPermutation(arr, start, end , n):
    if start == end:
        if arr[0] == '0':
            return
        permu_set.add((''.join(arr),n))
    else:
        for i in range(start,end):
            nn = n
            if not arr[start] == arr[i]:
                nn += 1
            arr[start], arr[i] = arr[i], arr[start]
            getPermutation(arr,start+1,end,nn)
            arr[start], arr[i] = arr[i], arr[start]

N, M = map(int,input().split())
arr = list(str(N))
permu_set = set()
tmp_list = []

flag = False
if len(arr) == 1 or (len(arr) == 2 and arr[1] == '0'):
    flag = True

getPermutation(arr, 0, len(arr),0)
sameBool = False
if len(set(arr)) != len(arr):
    sameBool = True
arr = list(str(N))
permu_set = sorted(list(permu_set))
anw = -1
if flag: permu_set = 0
while permu_set:
    c, k = permu_set.pop()
    if M == k:
        anw = int(c)
        break
    elif M > k:
        if sameBool or not (M-k)%2:
            anw = int(c)
            break

print(anw)