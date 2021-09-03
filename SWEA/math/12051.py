def check(N,D,G):
    if (G == 0 and D != 0) or (G == 100 and D != 100):
        return 'Broken'
    if N >= 100:
        return 'Possible'
    for i in range(N,0,-1):
        d=D*i/100
        if d.is_integer():
            return 'Possible'
    return 'Broken'

for tc in range(1,int(input())+1):
    N, D, G = map(int,input().split())
    print(f'#{tc} {check(N,D,G)}')