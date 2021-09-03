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

    def rot(self):
        self.append(self.popl())

    def __len__(self):
        return self.r-self.f

    def __repr__(self):
        return str(self.arr)

    def __getitem__(self, item):
        return self.arr[item]

for tc in range(1,int(input())+1):
    q = Q()
    for i in range(int(input())):
        q.append(i+1)
    while len(q) > 1:
        q.popl()
        q.rot()
    print(f'#{tc}', q[-1])