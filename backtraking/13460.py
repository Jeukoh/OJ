import sys; readline = sys.stdin.readline

class Board:
    def __init__(self,Map,Red,Blue,Hole):
        self.map = Map
        self.red = Red
        self.blue = Blue
        self.hole = Hole
        self.gole = [0,0]

    def move(self,dir):
        red_x = self.red[0]
        red_y = self.red[1]
        blue_x = self.blue[0]
        blue_y = self.blue[1]
        dx = dir[0]
        dy = dir[1]
        r_cnt = 0
        b_cnt = 0
        while True:
            if self.map[red_x+dx][red_y+dy] == '#':
                break
            if self.map[red_x+dx][red_y+dy] == 'O':
                self.gole[0] += 1
                break
            else:
                red_x += dx
                red_y += dy
                r_cnt += 1
        while True:
            if self.map[blue_x+dx][blue_y+dy] == '#':
                break
            if self.map[blue_x+dx][blue_y+dy] == 'O':
                self.gole[1] += 1
                break
            else:
                blue_x += dx
                blue_y += dy
                b_cnt += 1

        if red_x == blue_x and red_y == blue_y:
            if r_cnt > b_cnt:
                red_x -= dx
                red_y -= dy
            else:
                blue_x -= dx
                blue_y -= dy

        self.red = [red_x,red_y]
        self.blue = [blue_x,blue_y]



    def check(self):
        if self.gole != [0,0]:
            return True
        return False


N, M = map(int,readline().split())
Map = []
for _ in range(N):
    tmp_arr = list(readline().rstrip())
    if 'R' in tmp_arr:
        Red = [_,tmp_arr.index('R')]
    if 'B' in tmp_arr:
        Blue = [_,tmp_arr.index('B')]
    if 'O' in tmp_arr:
        Hole = [_,tmp_arr.index('O')]
    Map.append(tmp_arr)


a = Board(Map,Red,Blue,Hole)
# up left down right
dir = [[-1,0],[0,-1],[1,0],[0,1]]

stack = [[a.red, a.blue, 4]]
move_count = 1
visited = [[a.red, a.blue]]
flag2 = True
while move_count <= 10:
    tmp_stack = []
    while stack :
        action = stack.pop()
        for _ in range(4):
            if action[2]%2 == (_+1)%2 or action[2]==4:
                a.red = action[0]
                a.blue = action[1]
                a.gole = [0,0]
                a.move(dir[_])
                flag = True
                if a.check():
                    if a.gole == [1,0]:
                        print(move_count)
                        sys.exit()
                    else:
                        flag = False
                if [a.red, a.blue] not in visited and flag:
                    visited.append([a.red[:], a.blue[:]])
                    tmp_stack.append([a.red[:], a.blue[:], _])

    move_count += 1
    stack = tmp_stack
    if not tmp_stack:
        print(-1)
        sys.exit()

if move_count > 10:
    move_count = -1
print(move_count)


