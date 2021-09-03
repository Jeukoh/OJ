pascal_table = [[0]*10 for _ in range(10)]
pascal_table[0][0] = 1
for i in range(1,10):
    for j in range(i+1):
        pascal_table[i][j] = pascal_table[i-1][j] + pascal_table[i-1][j-1]
for tc in range(1,int(input())+1):
    N = int(input())
    print(f'#{tc}')
    for i in range(N):
        print(' '.join(str(pascal_table[i][j]) for j in range(i+1)))
