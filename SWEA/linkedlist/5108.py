class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist():
    def __init__(self):
        self.head = None

    def append(self,node):
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self,idx,node):
        if idx == 0:
            if self.head:
                node.next = self.head
                self.head = node
            else:
                self.append(node)
        else:
            cur_i = 0
            cur = self.head
            while cur_i < idx-1:
                cur = cur.next
                cur_i += 1
            b = cur
            a = cur.next
            b.next = node
            node.next = a

    def printer(self,idx):
        cur_i = 0
        cur = self.head
        while cur_i < idx:
            cur = cur.next
            cur_i += 1
        return cur.data


for tc in range(1,int(input())+1):
    N, M, L = map(int,input().split())
    K = list(map(int,input().split()))
    ll = linkedlist()
    for i in K:
        ll.append(Node(i))

    for _ in range(M):
        idx, v = map(int,input().split())
        ll.insert(idx,Node(v))

    print(f'#{tc}',ll.printer(L))

