from collections import deque
def solution(n, weak, dist):
    dist.sort(reverse=True)
    q = deque([weak]) #보수가 필요한 벽 위치들
    visited = set()
    visited.add(tuple(weak))
    for i in range(len(dist)): #일단 젤 쎈놈을 골라서
        d = dist[i]
        for _ in range(len(q)):
            current = q.popleft() #보수가 필요한 벽 위치들
            for p in current: # 하나씩 d로 긁어보자
                start = p
                end = (p + d) % n
                if start < end: # 긁고 남은 영역
                    rest = tuple(filter(lambda x: x < start or x > end, current))
                else:
                    rest = tuple(filter(lambda x: x < start and x > end, current))

                if len(rest) == 0: # 영역이 없으면 끝
                    return i + 1
                elif rest not in visited:
                    # 한번도 방문 안한 rest면 visited에 넣고 q에 넣어서
                    # 반복을 줄임 -> 어차피 긴거부터하닌까 나중에 여기서도 안된건
                    # 짧은 애들로도 안댐. q에 넣어서 고려할 이유가 없다.
                    visited.add(rest)
                    q.append(list(rest))
    return -1
if __name__ == '__main__':
    print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4]), 2)