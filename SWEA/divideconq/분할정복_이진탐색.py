def bisect(arr,N):
    low = 0
    high = len(arr)-1
    chef = None
    anwf = True
    while low <= high:
        mid = (low+high)//2

        if arr[mid] == N:
            if anwf:
                return True
            else:
                return False
        elif arr[mid] < N:
            low = mid+1
            if chef == True:
                anwf = False
            else:
                chef = True
        else:
            high = mid-1
            if chef == False:
                anwf = False
            else:
                chef = False

for tc in range(1,int(input())+1):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    B = list(map(int,input().split()))

    arr.sort()
    anw = 0
    for v in B:
        if bisect(arr,v): anw += 1

    print(f'#{tc}', anw)