import sys

t = int(sys.stdin.readline())
MAX = 1000000
# 단순하게 2중 for문 쓰면 안됨 O(N*2) -> t가 커질수록 시간초과
# a의 배수들은 모두 a를 약수로 가진다


f = [0] * (MAX + 1) # 각 인덱스의 약수의 합이 저장
g = [0] * (MAX + 1) # 누적합

for i in range(1, MAX + 1):
    j = 1
    while i * j <= MAX:
        f[i*j] += i # i의 배수들은 모두 i를 배수로 가짐
        j += 1
    # g(n) = g(n-1) + f(n)
    g[i] = g[i-1] + f[i]

for _ in range(t):
    n = int(sys.stdin.readline())
    print(g[n])