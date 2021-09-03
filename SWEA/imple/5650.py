from pprint import pprint
#dir 0 up 1 left 2 down 3 right
dx = (-1,0,1,0)
dy = (0,-1,0,1)
class Pinball():
    def __init__(self,Map,N):
        self.Map = Map
        self.now = [-1,-1]
        self.dir = -1
        self.score = -1
        self.flag= False
        self.wim = {i:[] for i in range(6,11)}
        for i in range(N+1):
            for j in range(N+1):
                if self.Map[i][j] in [6,7,8,9,10]:
                    self.wim[self.Map[i][j]].append([i,j])

    def start(self,loc,dir):
        self.now = loc[:]
        self.dir = dir
        self.score = 0
        start = loc[:]

        while True:
            #print(self.now,Map[self.now[0]][self.now[1]])
            self.move()
            if not self.check(start):
                break

        return self.score

    def check(self,start):
        #print('check',self.now, Map[self.now[0]][self.now[1]])
        #print('check', start)
        x, y = self.now
        # 자기자리 or 블랙홀이면 죽자
        if self.now == start or self.Map[x][y] == -1:
            return False
        if self.Map[x][y] == 0:
            return True
        # 방향 바꾸기
        if self.Map[x][y] in [1,2,3,4,5]:
            # up left down right
            # 0   1    2    3
            self.score += 1
            # 위로가는 경우, 1번 왼쪽, 4번 오른쪽
            if (Map[x][y] == 1 and self.dir == 1) or (Map[x][y] == 4 and self.dir == 3):
                self.dir = 0
                #print('ch up')
            # 오른쪽으로 가는 경우, 1번 아래, 2번 위
            elif (Map[x][y] == 1 and self.dir == 2) or (Map[x][y] == 2 and self.dir == 0):
                self.dir = 3
                #print('ch right')
            # 왼쪽으로 가는 경우, 4번 아래, 3번 위
            elif (Map[x][y] == 4 and self.dir == 2) or (Map[x][y] == 3 and self.dir == 0):
                self.dir = 1
                #print('ch left')
            # 아래로 가는 경우, 2번 왼쪽, 3번 오른쪽
            elif (Map[x][y] == 2 and self.dir == 1) or (Map[x][y] == 3 and self.dir == 3):
                self.dir = 2
                #print('ch down')
            else:
                #print('ch opp')
                self.dir = (self.dir+2)%4
            return True

        # 윔홀 통과하기
        if self.Map[x][y] in [6,7,8,9,10]:
            for tele in self.wim[self.Map[x][y]]:
                if [x,y] != tele:
                    self.now = tele[:]
                    break
            return True

    def move(self):
        #print(self.now,self.dir)
        self.now[0] += dx[self.dir]
        self.now[1] += dy[self.dir]

for tc in range(1,int(input())+1):
    N = int(input())
    Map = [[5]*(N+2)]
    for _ in range(N):
        Map.append([5]+list(map(int,input().split()))+[5])
    Map.append([5]*(N+2))
    #pprint(Map)

    max_score = 0
    a = Pinball(Map,N)

    for x in range(1,N+1):
        for y in range(1,N+1):
            for _ in range(4):
                if Map[x][y] == 0:
                    #print(x,y,_)
                    max_score = max(max_score,a.start([x,y],_))

    print(f'#{tc}', max_score)

    #score = a.start([4,9],2)