N = int(input())

#재귀를 사용해야함
# 1, 2, 3번 자리
# s에 N개 있을때 쌓여있을때, f로 보내는 함수
def Rec(N,s,f):
    # buffer는 중간
    b = 6-s-f
    if N <= 0:
        return None
    if N == 1:
        print(s, f)
        return None
    Rec(N-1,s,b)
    print(s, f)
    Rec(N-1,b,f)

print(2**N-1)
Rec(N,1,3)
