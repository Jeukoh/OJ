for tc in range(1,int(input())+1):
    Map = [list(map(int, input().split())) for _ in range(9)]

    anw = 1

    for _ in range(9):
        box_bool = [True]+[False]*9
        row_bool = [True]+[False]*9
        col_bool = [True]+[False]*9


        for i in range(9):
            row_bool[Map[_][i]] = True
            col_bool[Map[i][_]] = True
            a, b = _//3, _%3
            c, d = i//3, i%3
            box_bool[Map[3*a+c][3*b+d]] = True



        if not (all(row_bool) and all(col_bool) and all(box_bool)):
            anw = 0
            break

    print(f'#{tc} {anw}')