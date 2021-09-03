for tc in range(1,int(input())+1):
    N = int(input())
    anw = 'No'
    for i in range(1,10):
        for j in range(1,10):
            if i*j == N:
                anw = 'Yes'

    print(f'#{tc}', anw)