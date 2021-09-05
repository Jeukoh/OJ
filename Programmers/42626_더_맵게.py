from heapq import heapify, heappush, heappop


def solution(scoville, K):
    anw = 0
    heapify(scoville)
    while scoville[0] < K and len(scoville) >= 2:
        a = heappop(scoville)
        b = heappop(scoville)
        heappush(scoville, a + 2 * b)
        anw += 1

    if scoville[0] < K:
        return -1

    return anw