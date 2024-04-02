N, M = map(int, input().split())
memo = set([input() for _ in range(N)])
keyword = [input() for _ in range(M)]

for k in keyword:
    k = set(k.split(','))
    memo -= k
    print(len(memo))