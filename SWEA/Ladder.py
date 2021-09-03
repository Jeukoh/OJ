T = 10


def binary_search(arr,key):
    start = 0
    end = len(arr)
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid
        else:
            end = mid
    return False

for t in range(1,T+1):
    int(input())
    Map =[list(map(int,input().split())) for _ in range(100) ]

    N = len(Map[0])

    start = []
    for idx, value in enumerate(Map[0]):
        if value == 1:
            start.append(idx)

    for idx, value in enumerate(Map[-1]):
        if value == 2:
            r = len(Map)-1
            c = idx
            break

    while r > 0:
        #좌우 확인
        if 0 <= c-1 < N and Map[r][c-1]:
            c = start[binary_search(start,c)-1]
        elif 0 <= c+1 < N and Map[r][c+1]:
            c = start[binary_search(start,c)+1]
        r -= 1

    print(f'#{t} {c}')