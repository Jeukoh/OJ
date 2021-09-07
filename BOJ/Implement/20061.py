import sys; readline = sys.stdin.readline
from pprint import pprint
class Board:
    def __init__(self):
        self.board = [[0]*4 for _ in range(6)]
        self.score = 0

    def putblock(self,t,x,y):
        if t == 1:
            check = [(1,0)]
        elif t == 2:
            check = [(1,0),(1,1)]
        else:
            check = [(2,0),(1,0)]
            
        nx, ny = 0, y
        flag = True
        while flag and nx < 6:
            for _ in check:
                if 6 <= nx+_[0] or self.board[nx+_[0]][ny+_[1]]:
                    flag = False
                    break
            else:
                nx += 1
        for _ in check:
            self.board[nx+_[0]-1][ny+_[1]] = 1



    def scoring(self):
        for idx in range(2,6):
            if all(self.board[idx]):
                self.score += 1
                del self.board[idx]
                self.board.insert(0, [0,0,0,0])

    def regul(self):
        for idx in range(0,2):
            if any(self.board[idx]):
                del self.board[-1]
                self.board.insert(0, [0, 0, 0, 0])


    def ordering(self,t,x,y):
        self.putblock(t,x,y)
        self.scoring()
        self.regul()

    def printing(self):
        cnt = 0
        for idx in range(2, 6):
            cnt += sum(self.board[idx])
        return self.score, cnt


def rotate(x,y,t):
    if t == 1 or t == 2:
        nx, ny = y, 3-x
    else:
        nx, ny = y, 3-x-1
    nt = [1,3,2][t-1]
    return nt,nx,ny

N = int(readline().rstrip())
order = [list(map(int,readline().split())) for _ in range(N)]

A = Board()
B = Board()

for t,x,y in order:
    nt,nx,ny = (rotate(x,y,t))
    A.ordering(t,x,y)
    B.ordering(nt,nx,ny)

A_s, A_c = A.printing()
B_s, B_c = B.printing()
print(A_s+B_s)
print(A_c+B_c)

