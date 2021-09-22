import sys; readline = sys.stdin.readline
R,C,I = map(int,readline().split())
Map = [0]*257
max_h = 0
min_h = 256
total_block = I
for _ in range(R):
    sub_map = list(map(int,readline().split()))
    max_h = max(max_h,max(sub_map))
    min_h = min(min_h,min(sub_map))
    total_block += sum(sub_map)
    for j in sub_map:
        Map[j] += 1


min_time = 2*256*R*C
anw_height = min_h
# 모든 층을 height로 만들때 드는 시간
for height in range(min_h,max_h+1):
    time = 0
    if total_block < height*R*C:
        break
    for h in range(min_h,height):
        time += (height - h)*Map[h]
    for h in range(height+1,max_h+1):
        time += 2*(h-height)*Map[h]
    if min_time >= time:
        min_time = time
        anw_height = height

print(min_time, anw_height)