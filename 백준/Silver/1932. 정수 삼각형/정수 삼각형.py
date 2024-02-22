import sys

n = int(sys.stdin.readline())
triangle = [[] for _ in range(n)]
for i in range(n):
    triangle[i] = list(map(int, sys.stdin.readline().split()))

dp = [[0]*(i+1) for i in range(n)]
dp[0][0] = triangle[0][0]

j = 0
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j]+triangle[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1]+triangle[i][j]
        else:
            dp[i][j] = max(dp[i-1][j]+triangle[i][j], dp[i-1][j-1]+triangle[i][j]) 

print(max(dp[-1]))