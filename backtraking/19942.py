import sys
from copy import deepcopy
readline = sys.stdin.readline

N = int(readline())
min_list = list(map(int,readline().split()))
Yang_list = [0]*4
nutrient = []
Min_value = 500*15
for _ in range(N):
    nutrient.append(list(map(int,readline().split())))


Min_tmp = 0
anw_list = []
tmp = []
def dfs(k):
    global Min_tmp, Min_value, anw_list
    OK = True
    for idx,value in enumerate(Yang_list):
        if value < min_list[idx]:
            OK = False
            break

    if OK:
        if Min_tmp <= Min_value:
            Min_value = Min_tmp
            anw_list.append([Min_value]+tmp[:])

        return None
    else:
        for i in range(k,N):

            for idx in range(len(Yang_list)):
                Yang_list[idx] += nutrient[i][idx]

            Min_tmp += nutrient[i][-1]
            tmp.append(i)
            dfs(i+1)
            del tmp[-1]
            for idx in range(len(Yang_list)):
                Yang_list[idx] -= nutrient[i][idx]
            Min_tmp -= nutrient[i][-1]

dfs(0)
anw_list = sorted(anw_list,key=lambda x : x[0])
if anw_list != []:
    print(Min_value)
    print(' '.join(str(x+1) for x in anw_list[0][1:]))
else:
    print(-1)
