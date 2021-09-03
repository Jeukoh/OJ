def water_usage(P, Q, R, S, W):
    A = W * P
    B = Q + (W - R) * S if W > R else Q
    return min(A, B)

for tc in range(1,int(input())+1):
    P,Q,R,S,W = map(int,input().split())
    anw1 = P*W
    anw2 = Q
    if W > R:
        anw2 += (W-R)*S
    print(water_usage(P,Q,R,S,W))
    print(f'#{tc}', min(anw1,anw2))