import sys

def binary(array, target, left, right):
    result = 0
    while left <= right:
        mid = (left+right) // 2
        if array[mid] >= target:
            right = mid - 1
            result = mid
        else:
            left = mid + 1

    return result

N, M = map(int, sys.stdin.readline().split())

name = []
power = []
for i in range(N):
    n, p = sys.stdin.readline().split()
    name.append(n)
    power.append(int(p))

for i in range(M):
    c = int(sys.stdin.readline())
    answer = binary(power, c, 0, N-1)
    print(name[answer])
