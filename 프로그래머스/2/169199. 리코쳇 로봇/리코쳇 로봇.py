from collections import deque

def bfs(board, n, m, y, x):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((y, x, 0))
    visit = [[False]*m for _ in range(n)]
    visit[y][x] = True
    
    while q:
        y, x, c = q.popleft()
        if board[y][x] == 'G':
            return c
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            while 0<=nx<m and 0<=ny<n and board[ny][nx] != 'D':
                ny += dy[i]
                nx += dx[i]
            ny -= dy[i]
            nx -= dx[i]

            if not visit[ny][nx]:
                visit[ny][nx] = True
                q.append((ny, nx, c+1))
    return -1

def solution(board):
    n = len(board)
    m = len(board[0])
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                sy, sx = i, j
    
    return bfs(board, n, m, sy, sx)