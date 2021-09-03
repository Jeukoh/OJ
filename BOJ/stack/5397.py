import sys; readline=sys.stdin.readline
N = int(input())

for _ in range(N):
    loger = readline().rstrip()

    anw = []
    tmp_stack = []
    for i in loger:
        if i in '><-':
            if i == '<' and anw:
                tmp_stack.append(anw.pop())
            if i == '>' and tmp_stack:
                anw.append(tmp_stack.pop())
            if i == '-' and anw:
                anw.pop()

        else:
            anw.append(i)


    anw_str = ''.join(anw) + ''.join(tmp_stack[::-1])

    print(anw_str)