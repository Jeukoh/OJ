binhash = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110',
           '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

hash_code = {
     (2,1,1):0,
     (2,2,1):1,
     (1,2,2):2,
     (4,1,1):3,
     (1,3,2):4,
     (2,3,1):5,
     (1,1,4):6,
     (3,1,2):7,
     (2,1,3):8,
     (1,1,2):9
            }


def changecode1(code1):
    out = ''
    for s in code1:
        out += binhash[s]
    return changecode2(out.strip('0'))

def changecode2(code1):
    #2진수열에서 숫자들을 꺼냄
    #print(code)
    ret = []
    a = b = c = 0
    idx = len(code1) - 1
    while idx >= 0:
        if b and code1[idx] == '1':
            a += 1
        elif c and code1[idx] == '0':
            b += 1
        elif code1[idx] == '1':
            c += 1

        idx -= 1
        if a and b and c and code1[idx] == '0' or idx < 0:
            tmp = min(a,b,c)
            tmp2 = tuple(map(lambda x: x//tmp,(a,b,c)))
            ret.append(hash_code[tmp2])
            a = b = c = 0
            while idx >= 0 and code1[idx] == '0':
                idx -= 1

    code = ret[::-1]

    for n in range(len(ret) // 8):
        set_num.add(''.join(str(i) for i in code[8 * n:8 * (n + 1)]))


def check_num(num:str):
    ret = 0
    for _ in range(8):
        if _%2:
            ret += int(num[_])
        else:
            ret += 3*int(num[_])
    if ret%10:
        return False
    else:
        return True


for tc in range(1,int(input())+1):
    N, M = map(int,input().split())
    codes = set()
    for _ in range(N):
        codes.add(input().strip().strip('0'))

    codes.discard('')
    set_num = set()
    for code in list(codes):
        changecode1(code)

    set_num_val = filter(check_num,set_num)
    anw = 0
    for x in set_num_val:
        anw += sum(map(int,x))
    print('#{} {}'.format(tc, anw))