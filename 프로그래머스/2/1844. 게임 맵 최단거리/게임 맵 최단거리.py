from collections import deque

def bfs(maps, s_x, s_y, N, M):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False] * M for _ in range(N)]
    cnt = [[0] * M for _ in range(N)]
    q = deque()
    q.append((s_x, s_y))
    visited[s_y][s_x] = True
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<M and 0<=ny<N and maps[ny][nx] == 1 and not visited[ny][nx]:
                q.append((nx, ny))
                visited[ny][nx] = True
                cnt[ny][nx] = cnt[y][x] + 1
    return cnt

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    answer = bfs(maps, 0, 0, N, M)
    print(answer)
    
    if answer[N-1][M-1] == 0:
        return -1
    return answer[N-1][M-1] + 1
