T = int(input())


def move():
    global num
    Map[cur[0]][cur[1]] = num
    cur[0] += direc[0]
    cur[1] += direc[1]
    num += 1

def turn():
    global direc
    direc = [direc[1],-1*direc[0]]



for t in range(1,T+1):
    N = int(input())
    Map = [[0]*N for _ in range(N)]
    direc = [0, 1]
    cur = [0, 0]
    num = 1
    for _ in range(N-1):
        move()


    turn()
    K = N

    while K > 1:
        for _ in range(2):
            for x in range(K-1):
                move()
            turn()
        K -= 1
    move()

    print(f'#{t}')
    print('\n'.join(" ".join(str(x) for x in y)for y in Map))





