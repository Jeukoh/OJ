import sys; readline = sys.stdin.readline

nation_dict = {v:i for i,v in enumerate(readline().split())}
P_dict = {}
P_round = [0,0,0,0]
for _ in range(6):
    a, b, w, d, l = readline().split()
    a, b = nation_dict[a], nation_dict[b]
    if a > b:
        a, b = b, a
        w, l = l, w
    P_dict[(a,b)] = list(map(float,[w,d,l]))

versus=list(P_dict.keys())
versus.sort()
win_score = [0,0,0,0]
score = [3,1,0]

def whogetround(win_score,P):
    global P_round
    max_1 = max_2 = max_3 = -1
    max_1_idx = max_2_idx = max_3_idx = -1
    # print(win_score)
    for idx, x in enumerate(win_score):
        # print(idx)
        # print(max_1,max_2,max_3)
        # print(max_1_idx,max_2_idx,max_3_idx)
        if x > max_1:
            max_3 = max_2
            max_3_idx = max_2_idx
            max_2 = max_1
            max_2_idx = max_1_idx
            max_1 = x
            max_1_idx = idx
        elif max_1 >= x > max_2:
            max_3 = max_2
            max_3_idx = max_2_idx
            max_2 = x
            max_2_idx = idx
        elif max_2 >= x > max_3:
            max_3 = x
            max_3_idx = idx

    max_4_idx = 6-(max_1_idx+max_2_idx+max_3_idx)
    assert max_4_idx < 4, 'assert'

    if win_score.count(max_1) == 4:
        for _ in range(4):
            P_round[_] += P/2
    elif win_score.count(max_1) == 3:
        for _ in [max_1_idx,max_2_idx,max_3_idx]:
            P_round[_] += 2*P/3
    elif win_score.count(max_2) == 3:
        P_round[max_1_idx] += P
        for _ in [max_2_idx,max_3_idx,max_4_idx]:
            P_round[_] += P/3
    elif win_score.count(max_1) == 2:
        P_round[max_1_idx] += P
        P_round[max_2_idx] += P

    elif win_score.count(max_2) == 2:
        P_round[max_1_idx] += P
        for _ in [max_2_idx,max_3_idx]:
            P_round[_] += P/2
    else:
        P_round[max_1_idx] += P
        P_round[max_2_idx] += P

def dfs(i,win_score,P):
    global P_round
    if i == 6:
        whogetround(win_score,P)
        return
    a,b = versus[i]
    pp = P_dict[versus[i]]
    for _ in range(3):
        #print(i,win_score,pp)
        if pp[_] != 0:
            win_score[a] += score[_]
            win_score[b] += score[-1-_]
            P *= pp[_]
            dfs(i+1,win_score,P)
            win_score[a] -= score[_]
            win_score[b] -= score[-1-_]
            P /= pp[_]

dfs(0,win_score,1)
print('\n'.join(f'{x:.10f}' for x in P_round))