def angle90(N,i):
    anw = ''
    for _ in range(N-1,-1,-1):
        anw += Map[_][i]
    return anw

def angle180(N,i):
    anw = ''
    for _ in range(N-1,-1,-1):
        anw += Map[N-i-1][_]
    return anw

def angle270(N,i):
    anw = ''
    for _ in range(N):
        anw += Map[_][N-i-1]
    return anw


for tc in range(1,int(input())+1):
    N = int(input())
    Map = [input().split() for _ in range(N)]

    anw = []

    for _ in range(N):
        anw.append(' '.join([angle90(N,_),angle180(N,_),angle270(N,_)]))

    print(f'#{tc}')
    print('\n'.join(i for i in anw))




