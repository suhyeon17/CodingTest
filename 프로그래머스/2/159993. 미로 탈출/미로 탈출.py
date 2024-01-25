from collections import deque

def bfs(graph, x, y, e_x, e_y, n, m):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False] * m for _ in range(n)]
    
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = True
    cnt = 0
    
    while q:
        x, y, cnt = q.popleft()
        if x == e_x and y == e_y:
            return cnt
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and graph[nx][ny] != 'X' and visited[nx][ny] != True: 
                q.append((nx, ny, cnt + 1))
                visited[nx][ny] = True
    return -1
                
def solution(maps):
    n = len(maps)
    m = len(maps[0])

    for r in range(n):
        for c in range(m):
            if maps[r][c] == 'S':
                s_r, s_c = r, c
            elif maps[r][c] == 'E':
                e_r, e_c = r, c
            elif maps[r][c] == 'L':
                l_r, l_c = r, c
            else: continue
            
    sTol = bfs(maps, s_r, s_c, l_r, l_c, n, m)
    lToe = bfs(maps, l_r, l_c, e_r, e_c, n, m)
    
    if sTol == -1 or lToe == -1:
        return -1
    
    return sTol + lToe