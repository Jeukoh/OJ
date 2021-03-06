bin_hash = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
            '8': '1000', '9': '1001',
            'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

hash_code = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9
}


def change_code1(code: str):
    # 16진수를 2진수로 변환
    out = ''.join(bin_hash[s] for s in code)
    return change_code2(out.strip('0'))


def change_code2(code: str):
    # 2진수열에서 숫자들을 꺼냄
    # print(code)
    ret = []
    a = b = c = 0
    idx = len(code) - 1
    while idx >= 0:
        if b and code[idx] == '1':
            a += 1
        elif c and code[idx] == '0':
            b += 1
        elif code[idx] == '1':
            c += 1

        # print(idx,code[idx])
        # print(a,b,c)
        idx -= 1
        if a and b and c and code[idx] == '0' or idx < 0:
            tmp = min(a, b, c)
            tmp2 = tuple(map(lambda x: x // tmp, (a, b, c)))
            ret.append(hash_code[tmp2])
            # print(ret)
            a = b = c = 0
            while code[idx] == '0':
                idx -= 1

    code = ret[::-1]
    for n in range(len(ret) // 8):
        set_num.add(''.join(str(i) for i in code[8 * n:8 * (n + 1)]))


def check_num(num: str):
    ret = 0
    for _ in range(8):
        if _ % 2:
            ret += int(num[_])
        else:
            ret += 3 * int(num[_])
    if ret % 10:
        return False
    else:
        return True


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    codes = set()
    for _ in range(N):
        codes.add(input().strip())

    codes.remove('0' * M)
    set_num = set()
    codes = tuple(map(change_code1, codes))
    set_num_val = filter(check_num, set_num)
    anw = 0
    for x in set_num_val:
        anw += sum(map(int, x))
    print('#{} {}'.format(tc, anw))