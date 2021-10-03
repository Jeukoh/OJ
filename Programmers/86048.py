from collections import deque
def solution(enter, leave):
    answer = [0] * len(enter)

    room = deque([])

    en_cur = 0
    le_cur = 0

    while en_cur < len(enter) and le_cur < len(leave):
        print(en_cur,le_cur,room)
        if not room:
            room.append(enter[en_cur])
            en_cur += 1
            continue
        while en_cur < len(enter) and leave[le_cur] != room[-1]:
            room.append(enter[en_cur])
            en_cur += 1

        s = room.popleft()
        print(s)
        answer[s-1] = len(room)
        le_cur += 1

    print(room)

    return answer


if __name__ == '__main__':

    tests = ([[1,3,2],[1,2,3]],[[1,4,2,3],[2,1,3,4]])
    sols = ([0,1,1],[2,2,1,3])

    for idx, test in enumerate(tests):
        print(solution(test[0],test[1]),sols[idx])