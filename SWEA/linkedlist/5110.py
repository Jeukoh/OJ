class Node:
    def __init__(self,data):
        self.data = data
        self.l = None
        self.r = None

class linked:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.r = node
            node.l = self.tail
            self.tail = node

    def find_cur(self,value):
        cur = self.head
        if cur == None:
            return None
        while value >= cur.data:
            cur = cur.r
            if cur == None:
                return cur
        return cur

    def insert(self,arr):
        cur = self.find_cur(arr[0])
        if cur:
            big_prev_cur = cur.l
            for i in reversed(arr):
                cur.l = Node(i)
                prev_cur = cur
                cur = cur.l
                cur.r = prev_cur
            if big_prev_cur:
                cur.l = big_prev_cur
                big_prev_cur.r = cur
            else:
                self.head = cur

        else:
            for i in arr:
                self.append(Node(i))

    def printer(self):
        anw = []
        cur = self.tail
        cnt = 0
        while cnt < 10 and cur:
            anw.append(cur.data)
            cnt += 1
            cur = cur.l
        return ' '.join(map(str,anw))


for tc in range(1,int(input())+1):
    N, M = map(int,input().split())
    ll = linked()
    for _ in range(M):
        arr = list(map(int,input().split()))
        ll.insert(arr)

    print(f'#{tc}', ll.printer())