from collections import defaultdict
import sys;
sys.setrecursionlimit(10 ** 6)

from collections import defaultdict
import sys;

sys.setrecursionlimit(10 ** 6)


def solution(k, room_number):
    answer = []
    count_dict = defaultdict(int)

    def rec(son):
        # sonnom 들어오면 어느 방으로 안내해주어야할까요?
        # count_dict -> 손놈이 왔을 때 다음으로 갈 수 있는 방 가르킴
        # 0이면 빈 방임

        if not count_dict.get(son):
            answer.append(son)
            count_dict[son] = son + 1
            return son + 1

        count_dict[son] = rec(count_dict[son])
        return count_dict[son]

    for son in room_number:
        rec(son)

    # for son in room_number:
    #     while count_dict.get(son):
    #         count_dict[son] += 1
    #         son = son + count_dict[son] - 1
    #     count_dict[son] += 1
    #     answer.append(son)

    return answer



print(solution(10,[1,3,4,1,3,1]),[1,3,4,2,5,6])