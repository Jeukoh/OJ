def boyer_moore(pat,text):
    M = len(pat)
    N = len(text)
    i = 0
    anw = 0
    while i <= N-M:
        j = M-1
        while j >= 0:
            if pat[j] != text[i+j]:
                move = find(pat,text[i+M-1])
                break
            j = j -1
        if j == -1:
            anw += 1
            i += len(pat)
        else:
            i += move
    return anw


def find(pat,char):
    for i in range(len(pat)-2,-1,-1):
        if pat[i] == char:
            return len(pat)-i-1
    return len(pat)



for t in range(1,int(input())+1):
    text, pat = input().split()

    anw = boyer_moore(pat,text)

    print(f'#{t} {anw+len(text)-len(pat)*anw}')