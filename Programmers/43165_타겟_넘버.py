def solution(numbers, target):
    anw = 0
    Q = [0]
    i = 1
    ii = len(numbers)
    for i in range(ii):
        tmp_Q = []
        for v in Q:
            tmp_Q.append(v + numbers[i])
            tmp_Q.append(v - numbers[i])
        Q = tmp_Q[:]

    return Q.count(target)