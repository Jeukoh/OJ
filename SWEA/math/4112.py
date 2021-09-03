dp = [0]*142
for idx in range(142):
    dp[idx] = idx*(idx+1)//2

for tc in range(1,int(input())+1):
    a, b = map(int,input().split())
    if a > b:
        a, b = b, a
    a_flag, b_flag = True, True
    cur = 0
    while a_flag or b_flag:
        if dp[cur] < a <= dp[cur+1]:
            a_t = cur+1
            a_r = a-(dp[cur]+1)
            a_flag = False
        if dp[cur] < b <= dp[cur+1]:
            b_t = cur+1
            b_r = b-(dp[cur]+1)
            b_flag = False
        cur += 1
    if a_t == b_t:
        anw = abs(a_r-b_r)
    else:
        i = a_r+(b_t-a_t)
        if a_r <= b_r <= i:
            anw = abs(a_t-b_t)
        elif b_r > i:
            anw = abs(a_t-b_t) + b_r-i
        else:
            anw = abs(a_t-b_t) + a_r-b_r

    print(f'#{tc}', anw)