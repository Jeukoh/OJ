import sys; readline = sys.stdin.readline
r = 31
M = 1234567891
a = input()
text = readline().rstrip()
hash = 0
for idx,v in enumerate(text):
    hash = (hash+(ord(v)-ord('a')+1)*r**idx)%M

print(hash)