# from pprint import pprint
# import math
# anw = []
# cubic = [0]*3998
# for i in range(1,3998):
#     cubic[i] = i**3
#
#
#
#
#
# def findNum(obj,end):
#     # 주어진 obj과 end 대해서
#     # 가장 작은 a, c 값을 찾으면 a, c 리턴 없으면 0리턴
#     # a >= c 임을 조심
#
#     def binarySerach(start,end,v):
#         # 주어진 c에 대해서 가장 가까운 a 값을 찾자
#         # v는 obj - c**3 값
#         if end <= start+1:
#             return start
#
#         mid = (start+end)//2
#         if cubic[mid] > v:
#             anw = binarySerach(start,mid,v)
#         elif cubic[mid] < v:
#             anw = binarySerach(mid,end,v)
#         else:
#             anw = mid
#
#         return anw
#     for c in range(1,(end//2)+1):
#         v = obj-cubic[c]
#         end2 = end-c
#         if v <= 0:
#             break
#         a = binarySerach(1, end2, v)
#         if cubic[a] == v:
#             return a, c
#     else:
#         return 0,0
#     return -1,-1
#
#
# while True:
#     N = int(input())
#     if N == 0:
#         break
#
#     if (N**(1/3)).is_integer():
#         print('No value')
#         continue
#
#     # a + c + 2b = k
#     flag = False
#     for k in range(4, 4001):
#         for b in range(1,(k-4)//2+2):
#             obj = N*cubic[b]
#             # a + b 의 한도는
#             end = k-2*b
#             a, c = findNum(obj,end)
#             #print(a, c)
#             if a >= 1 and c >= 1:
#                 print(a,c,b)
#                 flag = True
#                 break
#         if flag:
#             break
#
#     if not flag:
#         print('No value')
#

