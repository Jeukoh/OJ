import sys

input = sys.stdin.readline
ppap = ["P", "P", "A", "P"]
stack = []
string = input().rstrip()
for i in range(len(string)):
    # 문자열 하나 추가
    stack.append(string[i])
    while len(stack) >= 4 and stack[-4:] == ppap:
        for _ in range(4):
            stack.pop()
        stack.append("P")
print("PPAP") if stack == ["P"] else print("NP")