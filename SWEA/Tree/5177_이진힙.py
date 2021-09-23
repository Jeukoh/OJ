def push(v):

    heap.append(v)
    hs = len(heap)-1

    c = hs; p = hs//2

    while p:
        if heap[c] < heap[p]:
            heap[c], heap[p] = heap[p], heap[c]
        else:
            break
        c = p
        p = c // 2


for tc in range(1,int(input())+1):
    heap = [0]
    input()
    for v in map(int,input().split()):
        push(v)
    anw = 0
    cur = len(heap)-1
    while cur:
        cur //= 2
        anw += heap[cur]

    print(f'#{tc}', anw)