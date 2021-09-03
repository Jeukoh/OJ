T = int(input())
i_list = []
const = 1000000007
for tc in range(T):
    i_list.append(list(map(int,input().split()))+list(map(int,input().split())))


def gdc(a,b):
    while b >= 1:
        a, b = b, a%b
    return a

for tc,I_list in enumerate(i_list):
    G = I_list[1]
    tmp = I_list[2:]
    anw = 0

    # 1. G로 안나눠지는 수 제거
    # (G보다 작은 수 자동 제거)
    lendp = 1001
    dp = [0]*lendp
    for v in tmp:
        if not v%G:
            for idx in range(1,v+1):
                if dp[idx] > 0:
                    x = gdc(idx,v)
                    dp[x] = (dp[x]+dp[idx])%const
        dp[v] += 1
    print(f'#{tc+1} {dp[G]}')