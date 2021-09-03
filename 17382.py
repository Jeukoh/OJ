import sys
readr = sys.stdin.readline

M,Q = map(int,readr().split())
print(M,Q)
r1,c1,r2,c2 = map(int,readr().split())

print(r1,c1,r2,c2)


def findnum(M,rs,cs): #r,c 좌표를 받고, 수열의 몇번째 자리인지 판단 후 -> 값 반환
    Snum = rs*M+cs




anw = []

for _ in range(1,10):
    for j in str(_):
        anw.append(j)

a = len(anw)
print(len(anw))

for _ in range(10,100):
    for j in str(_):
        anw.append(j)

print(len(anw))


for _ in range(100,1000):
    for j in str(_):
        anw.append(j)

