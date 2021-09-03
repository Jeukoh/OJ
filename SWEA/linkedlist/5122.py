class Node:
    def __init__(self,data):
        self.data = data
        self.l = None
        self.r = None

    def __str__(self):
        return str(self.data)

class linkroundl:
    def __init__(self):
        self.head = None
        self.cur = None
        self.cur_idx = 0
        self.cnt = 0
        self.tail = None

    def append(self,Node):
        self.cnt += 1
        if not self.head:
            self.head = Node
            self.tail = Node
            self.cur = Node
            self.cur_idx = 0
        else:
            self.tail.r = Node
            Node.l = self.tail
            self.tail = Node

    def curmove(self,idx):
        if idx == self.cur_idx:
            return
        elif idx < self.cur_idx:
            while idx != self.cur_idx:
                if self.cur.l == None:
                    return
                self.cur_idx -= 1
                self.cur = self.cur.l

        else:
            while idx != self.cur_idx:
                if self.cur.r == None:
                    return
                self.cur_idx += 1
                self.cur = self.cur.r


    def insert(self,idx,value):
        if self.cnt == 0:
            self.append(Node(value))
            return
        self.curmove(idx)
        NewNode = Node(value)
        if idx == 0:
            self.head = NewNode
            NewNode.r = self.cur
            self.cur.l = NewNode
            self.cur = self.cur.l
        else:
            if idx == self.cur_idx:
                # print(self.cur,self.cur.l)
                lnode = self.cur.l
                NewNode.r = self.cur
                self.cur.l = NewNode
                lnode.r = NewNode
                NewNode.l = lnode
                self.cur = self.cur.l
            else:
                NewNode.l = self.cur
                self.cur.r = NewNode
        self.cnt += 1

    def change(self,idx,value):
        self.curmove(idx)
        self.cur.data = value

    def delete(self,idx):
        self.curmove(idx)
        dn = self.cur
        if self.cnt == 1:
            self.head = None
            self.cur = None
        elif idx == self.cnt-1:
            ln = self.cur.l
            ln.r = None
            self.cur = self.cur.l
        elif idx == 0:
            rn = self.cur.r
            rn.l = None
            self.cur = self.cur.r
        else:
            ln = self.cur.l
            rn = self.cur.r
            ln.r = rn
            rn.l = ln
            self.cur = self.cur.r
        del dn
        self.cnt -= 1

    def __getitem__(self,idx):
        if self.cnt <= idx:
            return -1
        self.curmove(idx)
        return self.cur.data

    def __str__(self):
        self.curmove(0)
        return str(list(map((lambda x: self.__getitem__(x)), [i for i in range(self.cnt)])))

for tc in range(1,int(input())+1):
    N, M, L = map(int,input().split())
    ll = linkroundl()
    for i in list(map(int,input().split())):
        ll.append(Node(i))
    # print(ll)
    for _ in range(M):
        tmp = input().split()
        if tmp[0] == 'I':
            ll.insert(int(tmp[1]),int(tmp[2]))
        elif tmp[0] == 'C':
            ll.change(int(tmp[1]),int(tmp[2]))
        else:
            ll.delete(int(tmp[1]))
        # print(tmp)
        # print(ll.cur_idx, ll.cur,ll.head)
        # print(ll)
    print(f'#{tc}', ll[L])