import sys; readline = sys.stdin.readline

bingo = [list(map(int,readline().split())) for _ in range(5)]
bingo_dict = {}
for x in range(5):
    for y in range(5):
        bingo_dict[bingo[x][y]] = [x,y]

Number = []
for _ in range(5):
    Number.extend(list(map(int,readline().split())))

x_bool = [False]*5
y_bool = [False]*5
dia_bool = [False]*2

def check(x,y):
    for _ in range(5):
        if bingo[x][_] != 0:
            break
    else:
        x_bool[x] = True

    for _ in range(5):
        if bingo[_][y] != 0:
            break
    else:
        y_bool[y] = True

    if x==y:
        for _ in range(5):
            if bingo[_][_] != 0:
                break
        else:
            dia_bool[0] = True

    if y+x == 4:
        for _ in range(5):
            if bingo[_][4-_] != 0:
                break
        else:
            dia_bool[1] = True

def check_bool():
    anw = sum(x_bool)+sum(y_bool)+sum(dia_bool)
    if anw >= 3:
        return True
    else:
        return False

for idx,value in enumerate(Number):
     x,y = bingo_dict[value]
     bingo[x][y] = 0
     check(x,y)
     if check_bool():
         print(idx+1)
         break