import sys
from itertools import permutations 

N = int(sys.stdin.readline())
num_list = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

for _ in range(N):
    n, s, b = map(int, sys.stdin.readline().split())
    n = list(str(n))
    idx = 0
    for i in range(len(num_list)):
        s_cnt, b_cnt = 0, 0
        i -= idx
        for j in range(3):
            if str(num_list[i][j]) in n:
                if j == n.index(str(num_list[i][j])):
                    s_cnt += 1
                else:
                    b_cnt += 1
        if s_cnt != s or b_cnt != b:
            num_list.remove(num_list[i])
            idx += 1

print(len(num_list))