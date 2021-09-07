import sys; readline = sys.stdin.readline

class Dice:
    def __init__(self,N,M,x,y,Map):
        self.boundary = (N,M)
        self.x = x
        self.y = y
        self.Map = Map
        '''
            1
        3   0   2
            4
            5
        '''

        self.dev = [0,0,0,0,0,0]

    def change(self,x,y):
        if self.Map[x][y]:
            self.dev[-1] = self.Map[x][y]
            self.Map[x][y] = 0
        else:
            self.Map[x][y] = self.dev[-1]


    def devch(self,dir):
        tmp = self.dev[:]
        if dir == 0:
            self.dev = [tmp[4],tmp[0],tmp[2],tmp[3],tmp[5],tmp[1]]
        elif dir == 2:
            self.dev = [tmp[1], tmp[5], tmp[2], tmp[3], tmp[0], tmp[4]]
        elif dir == 1:
            self.dev = [tmp[2], tmp[1], tmp[5], tmp[0], tmp[4], tmp[3]]
        elif dir == 3:
            self.dev = [tmp[3], tmp[1], tmp[0], tmp[5], tmp[4], tmp[2]]

    def move(self,dir):
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        nx = self.x + dx[dir]
        ny = self.y + dy[dir]
        if (self.boundary[0] > nx >= 0 and self.boundary[1] > ny >= 0):
            self.x = nx
            self.y = ny
            self.devch(dir)
            self.change(nx,ny)
            print(self.dev[0])




N, M, x, y, K = map(int,readline().split())
Map = [list(map(int,readline().split())) for _ in range(N)]
order = list(map(int,readline().split()))

dir_dict = {4:2, 3:0, 2:1, 1:3}

dice = Dice(N,M,x,y,Map)

for i in order:
    dice.move(dir_dict[i])