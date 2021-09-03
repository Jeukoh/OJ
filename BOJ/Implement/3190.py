import sys; readline = sys.stdin.readline
from collections import deque

class Snake:

    def __init__(self,N,apple,L):
        self.N = N
        self.apple = apple
        self.dir = [0,1]
        self.locate = deque([[1,1]])
        self.time = 0
        self.L = L
        self.head = [1,1]
        self.alive = True



    def timegone(self):

        self.time += 1
        self.head[0] = self.head[0]+self.dir[0]
        self.head[1] = self.head[1]+self.dir[1]
        # 사망처리 1 나갔니?
        if not (0 < self.head[0] <= N and 0 < self.head[1] <=N):
            self.alive = False
            return
        # 머리가 몸에 닿았니?
        if self.head in self.locate:
            self.alive = False
            return

        #살았네? 위치 조정
        #한칸 이동
        self.locate.append(self.head[:])
        # 머리가 사과에 닿았니?
        if self.head in self.apple:
            # 사과 삭제
            self.apple.remove(self.head)
        # 아니면 꼬리 당겨오기
        else:
            self.locate.popleft()


        # 방향전환?
        if len(self.L):
            if self.time == int(self.L[0][0]):
                rot = self.L[0][1]
                del self.L[0]
                if rot == 'L':
                    self.dir = [-1*self.dir[1],self.dir[0]]
                else:
                    self.dir = [self.dir[1],-1*self.dir[0]]


N = int(input())
K_num = int(input())
apple = []
for _ in range(K_num):
    apple.append(list(map(int,readline().split())))

L_num = int(input())
L = []
for _ in range(L_num):
    L.append(list(readline().split()))

a = Snake(N,apple,L)

while a.alive:
    a.timegone()

print(a.time)