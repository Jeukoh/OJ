import sys; readline = sys.stdin.readline
N = int(input())
map_list = []
for _ in range(N):
    map_list.append([*map(int,readline().split())])

class Tonado:
    percent_table = [0.05,0.1,0.1,0.07,0.07,0.02,0.02,0.01,0.01]

    def __init__(self,N,map_list):
        self.map_list = map_list
        self.x = N//2
        self.y = N//2
        self.out = 0

    def move(self,move:tuple):
        dx,dy = move
        # 위치 이동 후, value 저장
        self.x += dx
        self.y += dy
        value = self.map_list[self.x][self.y]
        # 옮겨질 값을 할당
        move_list = list(map(lambda x : int(x*value), Tonado.percent_table))
        a = value-sum(move_list)
        # 옮겨질 자리 할당 7개
        #왼쪽 오른쪽이면
        if not dx:
            move_coord = [(0,2*dy),(1,dy),(-1,dy),(1,0),(-1,0),(2,0),(-2,0),(1,-dy),(-1,-dy)]
        else:
            move_coord = [(2*dx,0),(dx,1),(dx,-1),(0,1),(0,-1),(0,2),(0,-2),(-dx,1),(-dx,-1)]

        # 퍼센테이지 만큼 옮겨주고
        for idx,v in enumerate(move_coord):
            try:
                if self.x+v[0] < 0 or self.y+v[1] < 0:
                    raise IndexError
                self.map_list[self.x+v[0]][self.y+v[1]] += move_list[idx]
            except IndexError:
                self.out += move_list[idx]
        # 남은 a를 자리에
        try:
            if self.x+dx < 0 or self.y+dy <0:
                raise IndexError
            self.map_list[self.x+dx][self.y+dy] += a
        except IndexError:
            self.out += a
        # 다 옮겼으니 0으로 청소하고
        self.map_list[self.x][self.y] = 0

a = Tonado(N,map_list)

up,down,left,right = (-1,0),(1,0),(0,-1),(0,1)

for n in range(N//2):
    for i in range(n*2+1):
        a.move(left)
    for i in range(n*2+1):
        a.move(down)
    for i in range(n*2+2):
        a.move(right)
    for i in range(n*2+2):
        a.move(up)
for n in range(N-1):
    a.move(left)

print(a.out)




