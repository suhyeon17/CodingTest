def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])
    cnt = 0
    rm = set()
    
    while True:
        for r in range(m-1):
            for c in range(n-1):
                f = board[r][c]
                if f == 0:
                    continue
                if board[r+1][c] == f and board[r][c+1] == f and board[r+1][c+1] == f:
                    rm.add((r, c))
                    rm.add((r+1, c))
                    rm.add((r,c+1))
                    rm.add((r+1, c+1))
        #지우기
        if rm:
            cnt += len(rm)
            for i, j in rm:
                board[i][j] = 0
            rm = set()
        else: return cnt
        
        #보드 내리기
        while True:
            check = False
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] and board[i+1][j] == 0:
                        board[i+1][j] = board[i][j]
                        board[i][j] = 0
                        check = True
                        
            if not check: break
            