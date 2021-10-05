ml = [50000,10000,5000,1000,500,100,50,10]

for tc in range(1,int(input())+1):
    N = int(input())
    anw = [0]*8

    for i in range(8):
        anw[i] = N//ml[i]
        N %= ml[i]

    print(f'#{tc}\n'+' '.join(str(x) for x in anw))