import sys
from collections import Counter

N, M = map(int, sys.stdin.readline().split())
word_list = [sys.stdin.readline().rstrip() for _ in range(N)]
word_dict = Counter(word_list)
word_dict = sorted(word_dict.items(), key = lambda x:(-x[1], -len(x[0]), x[0]))

for word in word_dict:
    if len(word[0]) >= M:
        print(word[0])