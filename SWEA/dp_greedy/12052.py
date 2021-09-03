dx = [0,1,1]
dy = [1,0,1]

def greedy(X,Y):
    for x in range(X):
        for y in range(Y):
            if Map[x][y] == '#':
                Map[x][y] = '.'
                for _ in range(3):
                    if X>x+dx[_]>=0 and Y>y+dy[_]>=0 and Map[x+dx[_]][y+dy[_]] == '#':
                        Map[x+dx[_]][y+dy[_]] = '.'
                    else:
                        return 'NO'
    return 'YES'

for tc in range(1,int(input())+1):
    X, Y = map(int,input().split())

    Map = [list(input()) for _ in range(X)]


    print(f'#{tc} {greedy(X,Y)}')
