import itertools

n = int(input())

arr = []
for i in range(n):
    arr.append(i + 1)

for i in list(itertools.permutations(arr, n)):
    print(*i)