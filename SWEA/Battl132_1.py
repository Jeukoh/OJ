T = int(input())

for t in range(1,T+1):
    a, b = map(int,input().split())
    anw = (a+b)%24

    print(f'#{t} {anw}')