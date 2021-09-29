import sys; readline = sys.stdin.readline
import heapq
tc = int(input())
anw = []
for _ in range(tc):
    T = int(input())
    max_heap = []
    min_heap = []
    q = [readline().split() for __ in range(T)]
    visited = [False]*len(q)
    for id,v in enumerate(q):
        vv = int(v[1])
        if v[0] == 'I':
            heapq.heappush(max_heap,(-vv,id))
            heapq.heappush(min_heap, (vv,id))
            visited[id] = True
        elif vv == 1:
            while max_heap and not visited[max_heap[0][1]]:
                heapq.heappop(max_heap)
            if max_heap:
                visited[max_heap[0][1]] = False
                heapq.heappop(max_heap)

        elif vv == -1:
            while min_heap and not visited[min_heap[0][1]]:
                heapq.heappop(min_heap)
            if min_heap:
                visited[min_heap[0][1]] = False
                heapq.heappop(min_heap)


    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    anw.append(f'{-max_heap[0][0]} {min_heap[0][0]}' if max_heap and min_heap else 'EMPTY')

print('\n'.join(anw))