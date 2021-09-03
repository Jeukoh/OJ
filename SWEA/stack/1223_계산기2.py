push_prior = {'*':2, '+':1, '-':1, '/':2, '(':3, ')':3}
in_prior = {'*':2, '+':1, '-':1, '/':2, '(':0, ')':3}

def changetext(text):
    out = ''
    stack = []
    for i in text:
        if i not in push_prior:
            out += i
        else:
            if not stack:
                stack.append(i)
            elif i == ')':
                while stack[-1] != '(':
                    out += stack.pop()
                stack.pop()
            elif in_prior[stack[-1]] < push_prior[i]:
                stack.append(i)
            else:
                while stack and in_prior[stack[-1]] >= push_prior[i]:
                    out += stack.pop()
                stack.append(i)
    while stack:
        out += stack.pop()
    return out

def diy_eval(text):
    stack = []
    for i in text:
        if i not in push_prior:
            stack.append(int(i))
        else:
            b = stack.pop()
            a = stack.pop()
            if i == '+':
                tmp = a+b
            elif i == '-':
                tmp = a-b
            elif i == '*':
                tmp = a*b
            else:
                tmp = a/b
            stack.append(tmp)

    return int(stack[0])


for tc in range(1,10+1):
    N = int(input())
    text = input()
    a = diy_eval(changetext(text))
    print(f'#{tc} {a}')
