from math import gcd, ceil
import sys
AA,BB,x0,y0,vx,vy = map(int,input().split())


x1, y1 = x0+vx, y0+vy
A, B = (y1-y0), x0-x1
C = A*x0+B*y0
A = A*AA
B = B*BB

K = gcd(gcd(A,B),C)
A //= K
B //= K
C //= K
Gcd = gcd(A,B)

#A, B, C = abs(A), abs(B), abs(C)

def extended_gcd(a,b):
    x0, x1, y0, y1 = 1,0,0,1
    sa, sb = a, b
    while b != 0:

        n, a, b = a//b, b, a%b
        x0, x1 = x1, x0-n*x1
        y0, y1 = y1, y0-n*y1

    #print('-',x0,y0)
    if sa*x0+sb*y0 == 1:
        return x0, y0
    else:
        return -x0, -y0



if C==0:
    K = (A*B)//Gcd
    anw = abs(K//A) + abs(K//B) -1

elif not C%Gcd:
    K = C//Gcd
    if A < B:
        A, B = B, A
    T = extended_gcd(A,B)
    XX = T[0]*C
    YY = T[1]*C


    #print(XX,YY,T,A,B,C)

    if XX < 0 and B > 0:
        k = ceil(-XX/B)
        XX = XX + k*B//Gcd
        YY = YY - k*A//Gcd
    #print(XX, YY)
    if YY < 0 and A > 0:
        k = ceil(-YY/A)
        XX = XX - k*B//Gcd
        YY = YY + k*A//Gcd
    #print(XX, YY)

    if XX > abs(B) and YY > abs(A):
        k = min(XX//abs(B), YY//abs(A))
        if B < 0:
            XX = XX + k*B // Gcd
            YY = YY - k*A // Gcd
        else:
            XX = XX - k*B // Gcd
            YY = YY + k*A // Gcd

    anw = abs(XX)+abs(YY)-1

else:
    anw = -1

print(anw)
