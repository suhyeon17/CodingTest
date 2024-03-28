import sys
from collections import Counter

s = sys.stdin.readline().rstrip()
s = Counter(s)
s = dict(sorted(s.items(), key = lambda x : x[0]))

half = ''
for k, v in s.items():
    if v % 2 == 0:
        half += (k*(v//2))
        s[k] -= v
    else:
        half += (k*((v-1)//2))
        s[k] -= (v-1)

cnt = 0
odd  = ''
for k, v in s.items():
    if v != 0:
        cnt += 1
        odd += k

if cnt > 1:
    print("I'm Sorry Hansoo")

else: 
    if cnt == 1:
        print(half + odd + half[::-1])
    else:
        print(half + half[::-1])

