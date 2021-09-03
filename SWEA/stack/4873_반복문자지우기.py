i_list = []
T = int(input())
for _ in range(1,T+1):
    i_list.append((input()))

for idx, v in enumerate(i_list):
    stack = [0]
    for i in v:
        if i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)

    print(f'#{idx+1} {len(stack)-1}')

