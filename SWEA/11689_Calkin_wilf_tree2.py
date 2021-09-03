def con_frac(a,b):
    if a > b:
        a, b = b, a
    out = []
    while a:
        out.append(b//a)
        a, b = b%a, a

    if len(out)%2:
        out[-1] -= 1
        out.append(1)
    return sum(out)

T = int(input())
i_list = []
for tc in range(1,T+1):
    i_list.append(map(int,input().split()))
    
for tc in range(1,T+1):
    a, b = i_list[tc-1]
    print(f'#{tc}', (str(con_frac(a,b)-1)))

