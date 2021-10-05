def getIdxRunORTriplet(arr):
    ret = 6
    tmp = [0]*10
    for idx , v in enumerate(arr):
        tmp[v] += 1
        if tmp[v] == 3:
            return idx
        if v <= 7 and all(tmp[v:v+3]):
            return idx
        if 1 <= v <= 8 and all(tmp[v-1:v+2]):
            return idx
        if 2 <= v <= 9 and all(tmp[v-2:v+1]):
            return idx

    return ret

for tc in range(1,int(input())+1):
    arr = list(map(int,input().split()))

    a_arr = arr[::2]
    b_arr = arr[1::2]
    a_suc = getIdxRunORTriplet(a_arr)
    b_suc = getIdxRunORTriplet(b_arr)


    if a_suc < b_suc: anw = 1
    elif b_suc < a_suc: anw = 2
    else:
        if a_suc == 6:
            anw = 0
        else:
            anw = 1

    print(f'#{tc}', anw)