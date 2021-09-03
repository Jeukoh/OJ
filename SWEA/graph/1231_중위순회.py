class Node:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

class Tree():
    def __init__(self,N):
        self.node_list = [0]*(N+1)
        self.cur = 1

    def Treemake(self,data,left,right):
        self.node_list[self.cur] = Node(data,left,right)
        self.cur += 1

    def output(self,node_num):
        if node_num == None:
            return ''
        node = self.node_list[node_num]
        a = self.output(node.left)
        b = node.data
        c = self.output(node.right)
        return a+b+c

for tc in range(1,10+1):
    N = int(input())
    tree = Tree(N)
    for i in range(N):
        tmp = input().split()
        try:
            left = int(tmp[2])
        except:
            left = None
        try:
            right = int(tmp[3])
        except:
            right = None
        tree.Treemake(tmp[1],left,right)
    print(f'#{tc}', tree.output(1))