p = 'abadabaef'  # pattern
t = 'alksdabcdabcflaskjflkabadjsaflkjasdkdsajfabadabaeflksadjabadaksfjffsdafabadabaef'  # text


def BruteForce(pat, text):
    N = len(text)
    M = len(pat)
    i = j = 0
    anw = []
    while i < N:
        if pat[j] != text[i]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
        if j == M:
            anw.append([i - M, text[i - M:i]])
            j = 0

    return anw


p = 'abcdabcef'  # pattern
t = 'alksdabcdabcflaskjflkabcdjsaflkjasdkdsajfabcdabceflksadjabcdaksfjffsdafabcdabcef'


# print(BruteForce(p,t))

def KMP(pat, text):
    m, n = len(pat), len(text)
    next = [0] * (m + 1)
    # 전처리
    next[0] = -1
    i, j = 0, -1
    while i < m:
        while j >= 0 and pat[j] != pat[i]:
            j = next[j]
        i, j = i + 1, j + 1
        next[i] = j
    # 매칭
    i = j = 0
    anw = []
    while i < n:
        while j >= 0 and pat[j] != text[i]:
            j = next[j]
        i, j = i + 1, j + 1
        if j == m:
            anw.append([i - j, text[i - j:i]])
            j = 0

    return anw


p = 'abadabaef'
t = 'alksdabcdabcflaskjflkabadjsaflkjasdkdsajfabadabaeflksadjabadaksfjffsdafabadabaef'

print(KMP(p, t))


def BoyerMoore(pat, text):
    m, n = len(pat), len(text)
    next_dict = {}
    j = 0
    while j < m - 1:
        next_dict[pat[j]] = m - 1 - j
        j += 1
    i = 0
    anw = []
    while i <= n - m:
        j = m - 1
        while j >= 0 and text[i + j] == p[j]:
            j -= 1
        if j < 0:
            anw.append([i, text[i:i + m]])
            i += m
        else:
            i += next_dict.get(text[i + m - 1], m)
    return anw


p = 'abadabaef'
t = 'alksdabcdabcflaskjflkabadjsaflkjasdkdsajfabadabaeflksadjabadaksfjffsdafabadabaef'

# p = 'abab'
# t = 'baabbabab'




