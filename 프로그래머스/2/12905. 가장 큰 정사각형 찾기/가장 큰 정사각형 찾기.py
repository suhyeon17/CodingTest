def solution(board):
    n = len(board)
    m = len(board[0])
    
    dp = [[0]*m for _ in range(n)]
    dp[0] = board[0]
    for i in range(n):
        dp[i][0] = board[i][0]

    for r in range(1, n):
        for c in range(1, m):
            if board[r][c] == 1:
                dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
                
    answer = 0            
    for i in range(n):
        tmp = max(dp[i])
        if answer < tmp:
            answer = tmp
            
    return answer ** 2