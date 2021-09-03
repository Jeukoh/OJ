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
        self.tail = None
        self.cur = None
        self.cnt = 0

    def append(self,Node):
        if not self.head:
            self.head = Node
            self.tail = Node
            self.cur = Node
            Node.l = Node
            Node.r = Node
        else:
            self.tail.r = Node
            Node.l = self.tail
            Node.r = self.head
            self.tail = Node
        self.head.l = self.tail
        self.cnt += 1

    def insert(self):
        leftnode = self.cur.l
        NewNode = Node(leftnode.data+self.cur.data)
        leftnode.r = NewNode
        NewNode.l = leftnode
        if leftnode == self.tail:
            self.tail = NewNode
        self.cur.l = NewNode
        NewNode.r = self.cur
        self.cur = NewNode
        self.cnt += 1

    def __str__(self):
        anw = []
        cur = self.tail
        if self.cnt > 10:
            for _ in range(10):
                anw.append(cur.data)
                cur = cur.l
        else:
            for _ in range(self.cnt):
                anw.append(cur.data)
                cur = cur.l
        return ' '.join(map(str,anw))


for tc in range(1,int(input())+1):
    N, M, K = map(int,input().split())
    ll = linkroundl()
    for v in list(map(int,input().split())):
        ll.append(Node(v))

    for _ in range(K):
        for __ in range(M):
            ll.cur = ll.cur.r
        ll.insert()

    print(f'#{tc}', ll)