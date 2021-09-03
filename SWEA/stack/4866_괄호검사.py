i_list = []
T = int(input())
for _ in range(1,T+1):
    i_list.append((input()))

def verifi(text):
    stack = []
    anw = 1
    for i in text:
        try:
            if i in '({[':
                stack.append(i)
            if i in ')}]':
                b = stack.pop()
                if (b == '(' and i != ')') or (b == '{' and i != '}') \
                        or (b == '[' and i != ']'):
                    anw = 0
                    break
        except:
            anw = 0
            break

    if stack:
        anw = 0

    return anw

for _ in range(1,T+1):
    print(f'#{_} {verifi(i_list[_-1])}')