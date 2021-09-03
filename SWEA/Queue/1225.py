class Q():
    def __init__(self):
        self.arr = []
        self.f = 0
        self.r = 0

    def append(self,i):
        self.arr.append(i)
        self.r += 1

    def popl(self):
        ret = self.arr[self.f]
        self.f += 1
        return ret

    def rot(self,flag,i):
        if flag:
            self.append(max(0,self.popl()-i))
        else:
            self.append(self.popl())


    def __len__(self):
        return self.r-self.f

    def __repr__(self):
        return ' '.join(str(i) for i in self.arr[-8:])

    def __getitem__(self, item):
        return self.arr[item]

while True:
    try:
        tc = int(input())
        q = Q()
        for i in list(map(int,input().split())):
            q.append(i)
        i = 1
        while True:
            q.rot(True,i)
            i = (i)%5+1
            if q[-1] <= 0:
                break

        print(f'#{tc}', q)
    except EOFError:
        break
