import sys;
N = int(sys.stdin.readline().rstrip())
if (N-2)%7 == 0 or N%7 == 0:
    print('CY')
else:
    print('SK')