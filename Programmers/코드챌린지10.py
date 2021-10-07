def solution(n, m, x, y, queries):
    def checkwall(di, box):
        if di == 2:
            if box[0] == 0:
                return True
            else:
                return False
        elif di == 3:
            if box[2] == n:
                return True
            else:
                return False
        elif di == 0:
            return (True if box[1] == 0 else False)
        elif di == 1:
            return True if box[3] == m else False

    def querying(queri, box):
        if checkwall(queri[0], box):
            if queri[0] == 2:
                box[2] = min(box[2] + queri[1], n)
            elif queri[0] == 3:
                box[0] = max(box[0] - queri[1], 0)
            elif queri[0] == 0:
                box[3] = min(box[3] + queri[1], m)
            elif queri[0] == 1:
                box[1] = max(box[1] - queri[1], 0)
            # 박스를 늘려주어야 한다.
        else:
            # 박스 평행이동
            if queri[0] == 2:  # 위로
                box[0], box[2] = box[0] + queri[1], min(n, box[2] + queri[1])
                if box[0] >= n:
                    return False
            elif queri[0] == 3:  # 아래로
                box[0], box[2] = max(box[0] - queri[1], 0), box[2] - queri[1]
                if box[2] <= 0:
                    return False
            elif queri[0] == 0:
                box[1], box[3] = box[1] + queri[1], min(m, box[3] + queri[1])
                if box[1] >= m:
                    return False
            elif queri[0] == 1:
                box[1], box[3] = max(box[1] - queri[1], 0), box[3] - queri[1]
                if box[3] <= 0:
                    return False

        return box

    answer = -1
    box = [x, y, x + 1, y + 1]
    while queries:
        box = querying(queries.pop(), box)
        if not box:
            anw = 0
            break

    if box:
        anw = (box[2] - box[0]) * (box[3] - box[1])

    return anw

# def solution(n, m, x, y, queries):
#     answer = -1
#
#     bot = rig = -1
#     top, lef = n, m
#
#     r = c = 0
#     for q in queries:
#         if q[0] == 0:
#             c -= q[1]
#         if q[0] == 1:
#             c += q[1]
#         if q[0] == 2:
#             r -= q[1]
#         if q[0] == 3:
#             r += q[1]
#
#         bot = max(r, bot)
#         top = min(r, top)
#         rig = max(c, rig)
#         lef = min(c, lef)
#
#     print(bot, top)
#     print(rig, lef)
#
#     # x에 도착하는 것이 가능한 r들
#     # 4가지 케이스,
#     # r_min이랑 r_max가 부호가 같다면 하나만 생각하면 댄다. 음수면 min 양수면 max
#     # 1. r_min에'만' 가로 막히는 친구들 -> r_max로 바로 감 -> 아니넹 ㅋ
#     # 2. r_max에'만' 가로 막히는 친구들 -> r_min으로 바로 감
#     # 3. 둘다 안막히는 친구들 -> r_min 갔다가 r_max 감 ( 순서 상관 없음)
#     # 막힌다의 기준은? -> 0~r~n-1 까지 중 r+ bot or r+top 이 구간 밖이면 막히는 것
#     # 4. 둘다 막히는 친구들 ->  쿼리가 둘다 너무 크다면 가능할 수도.. 마지막으로 간 방향으로 갈 듯
#
#     # x 케이스 정리
#     x_cnt = 0
#     if bot * top > 0:
#         if top < 0:
#             bot = 0
#         else:
#             top = 0
#     # 위에 막히는 것의 idx 레인지 r = 0~-top까지 막힘 (0에 도달함)
#     topb = (0, min(-top, n - 1))
#     # 아래에 막히는 것의 idx 레인지 r = n-bot-1 ~ n-1
#     botb = (max(0, n - bot - 1), n - 1)
#     # 1,2,3,4 구하기
#     print(topb, botb)
#
#     return answer




