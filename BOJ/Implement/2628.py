import sys; readline = sys.stdin.readline
X, Y = map(int,readline().split())
X_l = [[0,X]]
Y_l = [[0,Y]]
for _ in range(int(input())):
    order, num = map(int,readline().split())

    if order == 1:
        new_X_l = []
        for i in X_l:
            if i[0] < num < i[1]:
                new_X_l.append([i[0],num])
                new_X_l.append([num,i[1]])
            else:
                new_X_l.append(i)

        X_l = new_X_l[:]

    if order == 0:
        new_Y_l = []
        for i in Y_l:
            if i[0] < num < i[1]:
                new_Y_l.append([i[0],num])
                new_Y_l.append([num,i[1]])
            else:
                new_Y_l.append(i)

        Y_l = new_Y_l[:]

max_x, max_y = 0, 0
for i in X_l:
    max_x = max(i[1]-i[0],max_x)
for i in Y_l:
    max_y = max(i[1]-i[0],max_y)

print(max_x*max_y)