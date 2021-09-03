for tc in range(1,int(input())+1):
    N = int(input())
    station = [0]*5001

    for _ in range(N):
        A, B = map(int,input().split())
        for i in range(A,B+1):
            station[i] += 1


    P = int(input())
    output = [0]*P
    for _ in range(P):
        output[_] = station[int(input())]

    print(f'#{tc} {" ".join(str(i) for i in output)}')