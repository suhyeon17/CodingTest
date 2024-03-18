import sys
from itertools import permutations

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
op = list(map(int, sys.stdin.readline().rstrip().split()))
op = op[0]*'+ ' + op[1]*'- ' + op[2]*'* ' + op[3]*'// '
op = op.split()

answer = []
for per in permutations(op, len(op)):
    result = nums[0]
    for i in range(len(op)):
        if per[i] == '+':
            result += nums[i+1]
        elif per[i] == '-':
            result -= nums[i+1]
        elif per[i] == '*':
            result *= nums[i+1]
        else:
            if result < 0:
                result = (abs(result) // nums[i+1]) * (-1)
            else:
                result //= nums[i+1]
    answer.append(result)

print(max(answer))
print(min(answer))
    