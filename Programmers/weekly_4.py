def solution(table, languages, preference):
    score = []
    weight = {i: v for i, v in zip(languages, preference)}
    print(weight)
    for i in table:
        k = i.split()
        t = k[0]
        tmp = 0
        for idx, v in enumerate(k[-1:0:-1]):
            tmp += weight.get(v, 0) * (idx + 1)

        score.append([tmp, t])

    score.sort(key=lambda x: (-x[0], x[1]))

    return score[0][1]