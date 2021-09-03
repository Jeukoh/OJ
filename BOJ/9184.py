import sys

def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20,20,20)
    elif W[a][b][c] != 0:
            return W[a][b][c]
    else:
        if a < b and b < c:
            W[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
        else:
            W[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
    return W[a][b][c]

readr = sys.stdin.readline

W = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
W[0][0][0] = 1
W[20][20][20] = 1048576

while True:
    a,b,c = list(map(int,readr().split()))
    if [a,b,c] == [-1,-1,-1]:
        break
    print("w({}, {}, {}) = {}".format(a,b,c,w(a,b,c)))
