import sys; readline = sys.stdin.readline
R,C,I = map(int,readline().split())
Map = []
max_h = 0
min_h = 256
total_block = I
for _ in range(R):
    sub_map = list(map(int,readline().split()))
    max_h = max(max_h,max(sub_map))
    min_h = min(min_h,min(sub_map))
    Map.append(sub_map)
    total_block += sum(sub_map)


min_time = 2*256*R*C
anw_height = min_h
# 모든 층을 height로 만들때 드는 시간
for height in range(min_h,max_h+1):
    now_I = I
    time = 0

    if total_block < height*R*C:
        break

    for r in range(R):
        for c in range(C):
            now_I += Map[r][c] - height
            if Map[r][c] > height:
                time += 2*(Map[r][c]-height)
            elif Map[r][c] < height:
                time += height-Map[r][c]

    if now_I < 0:
        continue
    if min_time >= time:
        min_time = min(min_time,time)
        anw_height = height

print(min_time, anw_height)