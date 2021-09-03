hash_dict1 = {(2,1,1): 0, (2,2,1): 1, (1,2,2): 2,   (4,1,1): 3, (1,3,2): 4, (2,3,1): 5, (1,1,4): 6, (3,1,2): 7, (2,1,3): 8, (1,1,2): 9 }
bin_dict1 = { '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'  }

for t in range(1, int(input()) + 1):
    N, M = list(map(int, input().split()))
    code = [input() for _ in range(N)]
    input_list = list(set(code))
    anw = 0
    visited = []
    for l in input_list:
        line = ""
        for i in l:
            line += bin_dict1[i]
        line = line.rstrip('0')
        a = b = c = 0
        num = []
        for idx in range(len(line) - 1, -1, -1):
            if b == 0 and line[idx] == '1':
                c += 1
            elif line[idx] == '0' and a == 0:
                b += 1
            elif line[idx] == '1':
                a += 1
            elif line[idx] == '0':
                if line[idx - 1] == '1':
                    gcd = min(a, b, c)
                    num.append(hash_dict1[(a//gcd,(b//gcd),c//gcd)])
                    a = b = c = 0
                    if len(num) == 8:
                        if ((num[0] + num[2] + num[4] + num[6]) + (num[1] + num[3] + num[5] + num[7]) * 3) % 10 == 0:
                            if num not in visited:
                                visited.append(num)
                                anw += sum(num)
                        num = []

    print('#{} {}'.format(t,anw))