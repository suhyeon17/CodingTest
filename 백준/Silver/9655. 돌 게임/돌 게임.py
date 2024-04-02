N = int(input())

if N == 1:
    print('SK')
elif N == 2:
    print('CY')
elif N == 3:
    print('SK')
else:
    dp = [-1] * (N+1)

    dp[1] = 1 #상근
    dp[2] = 0 #창영
    dp[3] = 1 #상근

    for i in range(4, N+1):
        if dp[i-1] == 1 or dp[i-3] == 1:
            dp[i] = 0
        else:
            dp[i] = 1

    if dp[N] == 1:
        print("SK")

    else:
        print("CY")
