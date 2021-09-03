from collections import deque, defaultdict
from pprint import pprint

class board_piece:
    def __init__(self,piece):
        self.piece = piece

    def __str__(self):
        return '\n'.join(''.join(str(x) for x in y) for y in self.piece[0])


class table_piece:
    def __init__(self,piece):
        self.piece = self.getrotate(piece)

    def getrotate(self,piece):
        def rotate(piece):
            r, c = len(piece), len(piece[0])
            ret = [[0]*(r) for _ in range(c)]

            for x in range(c):
                for y in range(r):
                    ret[x][y] = piece[r-1-y][x]
            return ret

        pieces = [piece]
        for _ in range(3):
            new_piece = rotate(pieces[-1])
            if new_piece in pieces:
                break
            pieces.append(new_piece)

        return pieces

    def __str__(self):
        return '\n\n'.join('\n'.join(''.join(str(x) for x in y) for y in z) for z in self.piece)

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(x,y,N,board):
    if board == game_board:
        flag = True
    else:
        flag = False
    Map = board
    coords = [[x,y]]
    Q = deque([[x,y]])
    if flag:
        while Q:
            x,y = Q.popleft()
            for _ in range(4):
                nx,ny = x+dx[_], y+dy[_]
                if N>nx>=0 and N>ny>=0 and not Map[nx][ny]:
                    Map[nx][ny] = 1
                    Q.append([nx,ny])
                    coords.append([nx,ny])
    else:
        while Q:
            x,y = Q.popleft()
            for _ in range(4):
                nx,ny = x+dx[_], y+dy[_]
                if N>nx>=0 and N>ny>=0 and Map[nx][ny]:
                    Map[nx][ny] = 0
                    Q.append([nx,ny])
                    coords.append([nx,ny])

    return coords


def makepiece(coords):
    min_x = min_y = float('inf')
    max_x = max_y = 0
    for _ in coords:
        max_x = max(_[0],max_x)
        max_y = max(_[1], max_y)
        min_x = min(_[0],min_x)
        min_y = min(_[1],min_y)

    piece = [[0]*(max_y-min_y+1) for _ in range(max_x-min_x+1)]

    for _ in coords:
        piece[_[0]-min_x][_[1]-min_y] = 1

    return piece

def solution(game_board, table):
    N = len(game_board)
    board_pieces = defaultdict(list)
    for x in range(N):
        for y in range(N):
            if not game_board[x][y]:
                game_board[x][y] = 1
                coords = bfs(x,y,N,game_board)
                piece = makepiece(coords)
                board_pieces[len(coords)].append(board_piece(piece))

    table_pieces = defaultdict(list)
    for x in range(N):
        for y in range(N):
            if table[x][y]:
                table[x][y] = 0
                coords = bfs(x,y,N,table)
                piece = makepiece(coords)
                table_pieces[len(coords)].append(table_piece(piece))

    anw = 0
    for i, b_p in board_pieces.items():
        t_p = table_pieces.get(i)
        if t_p:
            b_visit = [True]*len(b_p)
            t_visit = [True]*len(t_p)
            for ii, x in enumerate(b_p):
                for jj, y in enumerate(t_p):
                    if x.piece in y.piece and b_visit[ii] and t_visit[jj]:
                        anw += i
                        b_visit[ii] = False
                        t_visit[jj] = False


    return anw

if __name__ == '__main__':

    test_case = [ ([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
                  [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0],
                   [0, 1, 0, 0, 0, 0]],14),
                  ([[0,0,0],[1,1,0],[1,1,1]],[[1,1,1],[1,0,0],[0,0,0]],0)
                  ]

    for game_board, table, result in test_case:
        if solution(game_board, table) == result:
            print('정답')
        else:
            print('땡')

