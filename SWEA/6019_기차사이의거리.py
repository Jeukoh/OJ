T = int(input())

for t in range(1,T+1):
    D,A,B,F = map(int,input().split())

    col_t = D/(A+B)

    print(f'#{t} {format(F*col_t,".10f")}')