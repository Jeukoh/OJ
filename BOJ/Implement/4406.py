import sys; readline = sys.stdin.readline
import math

while True:
    a,b,s,m,n = map(int,readline().split())
    if [a,b,s,m,n] == [0,0,0,0,0]:
        break

    dx = a*m
    dy = b*n

    seta = math.atan(dy/dx)*180/math.pi
    v = math.sqrt((dx**2+dy**2))/s

    print(f'{seta:.2f} {v:.2f}')