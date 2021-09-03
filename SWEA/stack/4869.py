i_list = []
for tc in range(1,int(input())+1):
    i_list.append(int(input()))

max_inp = max(i_list)//10

dp = [0]*(max_inp+1)
dp[1],dp[2] = 1, 3

for i in range(3,max_inp+1):
    dp[i] = dp[i-1]+2*dp[i-2]

for idx, v in enumerate(i_list):
    print(f'#{idx+1} {dp[v//10]}')