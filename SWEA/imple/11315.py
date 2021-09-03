dx = [-1,0,1,0,-1,1]
dy = [0,-1,0,1,1,1]

def aa():
    for _ in range(6):
        for i in dico:
            cnt = 0
            nx, ny = i[0], i[1]
            while dico.get((nx,ny)):
                nx += dx[_]
                ny += dy[_]
                cnt += 1
            if cnt >= 5:
                return 'YES'
    return 'NO'

for tc in range(1,int(input())+1):
    N = int(input())
    dico = {}
    for i in range(N):
        for j, value in enumerate(list(input())):
            if value == 'o':
                dico[(i,j)] = 1


    print(f'#{tc}', aa())


