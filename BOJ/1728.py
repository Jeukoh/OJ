import sys
def vel(locarr,inilo,time):
    anw = []
    for i in locarr:
        if type(i) is int:
            anw.append((i-inilo)/time)
    return set(anw)
readr = sys.stdin.readline
N = int(readr())
locatearr = []
for _ in range(N+1):
    locatearr.append(list(map(int,readr().split())))
anw = dict()
for _ in range(N):
    inilo = locatearr[0][0]
    av = vel(locatearr[1],inilo,1)
    if len(av) == 1:
        anw[inilo] = int(av.pop())
    else:
        for cor in range(2,N+1):
            bv = vel(locatearr[cor],inilo,cor)
            av = av&bv
            if len(av) == 1:
                anw[inilo] = int(av.pop())
                break
    for time in range(0,N+1):
        locatearr[time].remove(inilo + time*anw[inilo])


anw = sorted(anw.items(),key=lambda x: x[0])
for i in anw:
    print(' '.join(str(j) for j in i))
