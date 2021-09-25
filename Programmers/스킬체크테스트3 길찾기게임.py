from collections import deque
import sys;
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    ni = [x[:] + [idx + 1] for idx, x in enumerate(nodeinfo)]
    ni.sort(key=lambda x: (-x[1], x[0]))
    # x좌표,y좌표,value
    rank_table = sorted(list(set(x[1] for x in nodeinfo)),reverse=True)
    preorder = []
    postorder = []

    def recur(subtree,levelcur):
        x,rank,v = subtree.popleft()
        preorder.append(v)
        for i in range(len(subtree)):
            if subtree[i][1] == rank_table[levelcur+1]:
                if subtree[i][0] < x:
                    recur(deque([y for y in subtree if y[0] < x]),levelcur+1)
                elif subtree[i][0] > x:
                    recur(deque([y for y in subtree if y[0] > x]), levelcur+1)

        postorder.append(v)
    recur(deque(ni),0)
    return [preorder,postorder]




if __name__ == '__main__':
    print(
        solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])
    ,   [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]])