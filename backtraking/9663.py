import sys; readline = sys.stdin.readline
N = int(readline())
visit_a = [True]*N
visit_b = [True]*(2*N-1) #오른쪽위  x+y=?
visit_c = [True]*(2*N-1) #오른쪽 아래 x-y+(N-1)=?
def dfs(k):
    global anw
    if k == N:
        anw += 1
        #anw_list.append(tmp[:])
        return None
    for i in range(N):
        if visit_a[i] and visit_b[k+i] and visit_c[k-i+N-1]:
            #tmp.append([k,i])
            visit_a[i], visit_b[i+k], visit_c[k-i+N-1] = False, False, False
            dfs(k+1)
            #tmp.remove([k,i])
            visit_a[i], visit_b[i + k], visit_c[k - i + N - 1] = True, True, True




anw = 0
#anw_list = []
#tmp = []


dfs(0)

print(anw)

# anw = 0
# if N%2:
#     dfs(0)
# else:
#     for i in range(N//2):
#         if visit_a[i] and visit_b[i] and visit_c[-i+N-1]:
#             visit_a[i], visit_b[i], visit_c[-i+N-1] = False, False, False
#             dfs(1)
#             visit_a[i], visit_b[i], visit_c[-i + N - 1] = True, True, True
#     anw *= 2
#
# print(anw)

