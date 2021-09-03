import sys

readline = sys.stdin.readline
N = int(readline())
len_road = list(map(int,readline().split()))
price_gas = list(map(int,readline().split()))

price_gas = price_gas[:-1]
total_pay = 0
min_gas = price_gas[0]
min_corsor = 0
for idx,value in enumerate(price_gas):
    if value < min_gas:
        min_corsor = idx
        min_gas = value
    total_pay += min_gas*len_road[idx]




print(total_pay)