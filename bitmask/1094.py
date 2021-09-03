N = int(input())

def countbit(N):
    cnt = 0
    while N>0:
        N = N&(N-1)
        cnt +=1
    return cnt

print(countbit(N))