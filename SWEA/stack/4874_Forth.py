def cacl(text):
    stack = []
    try:
        for i in text:
            if i in '+*-/':
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    stack.append(a+b)
                elif i == '-':
                    stack.append(a-b)
                elif i == '*':
                    stack.append(a*b)
                else:
                    stack.append(a//b)
            elif i == '.':
                anw = int(stack.pop())
                break
            else:
                stack.append(int(i))
    except:
        anw = 'error'

    if stack:
        anw = 'error'

    return anw

for tc in range(1,int(input())+1):
    text = input().split()
    print(f'#{tc} {cacl(text)}')