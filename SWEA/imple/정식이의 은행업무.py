
def ltn(arr,mode):
    if mode == 2:
        return int(''.join(str(x) for x in arr),2)
    if mode == 3:
        return int(''.join(str(x) for x in arr),3)

for tc in range(1,int(input())+1):
    binarynum = list(map(int,input().strip()))
    cubnum = list(map(int,input().strip()))
    pos_num = []
    anw = 0
    for i in range(len(binarynum)):
        k = binarynum[i]
        binarynum[i] = 1-k
        pos_num.append(ltn(binarynum,2))
        binarynum[i] = k

    for i in range(len(cubnum)):
        k = cubnum[i]
        for x in range(3):
            if k == x:
                continue
            cubnum[i] = x
            tmp = ltn(cubnum, 3)
            if tmp in pos_num:
                anw = tmp
                break
        cubnum[i] = k

        if anw:
            break

    print(f'#{tc}', anw)