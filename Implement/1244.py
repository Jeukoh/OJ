import sys; readline = sys.stdin.readline
switch_len = int(input())
switch = [0]+list(map(lambda x: -1 if x =='0' else 1,readline().split()))
N = int(input())
for _ in range(N):
    g, num = map(int,readline().split())

    # 남자
    if g == 1:
        for idx in range(num,len(switch),num):
            switch[idx] *= -1
    if g == 2:
        k = 0
        while num-k > 0 and num+k < len(switch):
            if switch[num+k] == switch[num-k]:
                k += 1
            else:
                break
        for idx in range(num-k+1,num+k):
            switch[idx] *= -1

switch = list(map(lambda x: 0 if x==-1 else 1,switch[1:]))
for _ in range(switch_len//20+1):
    print(' '.join(str(x) for x in switch[_*20:(_+1)*20]))