import sys
from itertools import combinations

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
items = list(map(int, sys.stdin.readline().rstrip().split()))
items.sort()
s, e, cnt = 0, N-1, 0

while s < e:
    if items[s] + items[e] == M:
        cnt += 1
        s += 1
        e -= 1
    elif items[s] + items[e] > M:
        e -= 1
    else:
        s += 1

print(cnt)