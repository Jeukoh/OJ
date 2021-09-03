import sys

def midsort(arr):
    tmp = sorted(arr)
    anw = tmp[:]
    for i in range(len(tmp)):
        if i%2:
            anw[i] = tmp[-(i//2)-1]
        else:
            anw[i] = tmp[i//2]
    return anw

def check(i,j): # i에서 j 로 가도 되겠니?
    if not box[i]:
        return False
    mid_start = box[i][-1]
    tmp = box[j][:]
    tmp.append(mid_start)
    if midsort(tmp)[:-1] == box[j]:
        return True
    else:
        return False

N = int(input())
box =[midsort([i for i in range(1,N+1)]),[],[]]
anw = [[0,0]]
box2 = [[i for i in range(1,N+1)],[],[]]


# while True:
#     if len(box[2]) == N or len(box[1]) == N:
#         print(anw)
#         sys.exit()
#
#     for x in range(3):
#         for y in range(2,-1,-1):
#             print(x, y, box)
#             if x != y and check(x,y):
#                 tmp = box[x].pop()
#                 box[y].append(tmp)
#                 anw.append([x+1,y+1])
#                 visited.append([sum(1<<(i-1) for i in box[0]),sum(1<<(i-1) for i in box[1]),sum(1<<(i-1) for i in box[2])])


while True:
    print(box)
    #print(box2)
    x,y = map(int,input().split())
    if x == 100:
        break
    x -= 1
    y -= 1

    if x != y and check(x, y):
        tmp = box[x].pop()
        tmp2 = box2[x].pop()
        box[y].append(tmp)
        box2[y].append(tmp2)
        if anw[-1] == [y+1,x+1]:
            anw.pop()
        else:
            anw.append([x+1,y+1])


    else:
        print('불가능')

print(*anw[1:], end='\n')
print(len(anw)-1)
