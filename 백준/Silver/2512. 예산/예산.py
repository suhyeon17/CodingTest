import sys

N = int(sys.stdin.readline())
budget = list(map(int, sys.stdin.readline().rstrip().split()))
budget.sort()
total = int(sys.stdin.readline())
total_budget = sum(budget)

if total_budget <= total:
    print(budget[-1])
else:
    for i, b in enumerate(budget):
        if total // (N-i) > b:
            total -= b
        else:
            break

    print(total // (N-i))

