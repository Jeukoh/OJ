T = int(input())

def value_route(x,y):
    return abs(x[0]-y[0])+abs(x[1]-y[1])


def sol(N,job,home,sonnoms):

    min_value = [N*200]
    visit = [False]*N

    def dfs(k,tmp_min_value,j):
        #print(k,tmp_min_value,j)
        if k == N:
            tmp_min_value += value_route(home,sonnoms[j])
            if tmp_min_value >= min_value[0]:
                return None
            else:
                min_value[0] = tmp_min_value
                return None
        if tmp_min_value >= min_value[0]:
            return None

        for i in range(N):
            if not visit[i]:
                if k == 0:
                    tmp_min_value += value_route(job,sonnoms[i])
                    visit[i] = True
                    dfs(k+1,tmp_min_value,i)
                    visit[i] = False
                    tmp_min_value -= value_route(job,sonnoms[i])
                else:
                    tmp_min_value += value_route(sonnoms[j],sonnoms[i])
                    visit[i] = True
                    dfs(k+1,tmp_min_value,i)
                    visit[i] = False
                    tmp_min_value -= value_route(sonnoms[j],sonnoms[i])



    dfs(0,0,0)
    return min_value


for _ in range(T):
    N = int(input())
    input_list = list(map(int,input().split()))

    job, home = input_list[0:2], input_list[2:4]
    sonnoms = []
    for i in range(4,len(input_list),2):
        sonnoms.append(input_list[i:i+2])

    anw = sol(N,job,home,sonnoms)[0]

    print(f'#{_+1} {anw}')

