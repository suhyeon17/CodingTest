import sys
from collections import deque

def bfs(x, y, e_x, e_y, N):
    dx = [-2, -2, 2, 2, -1, 1, -1, 1]
    dy = [-1, 1, -1, 1, -2, -2, 2, 2]
    visited = [[False] * N for _ in range(N)]
    q = deque()
    q.append((x, y, 0))
    visited[y][x] = True

    while q:
        x, y, cnt = q.popleft()
        if x == e_x and y == e_y:
            return cnt
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N and not visited[ny][nx]:
                q.append((nx, ny, cnt+1))
                visited[ny][nx] = True

T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    x, y = map(int, sys.stdin.readline().rstrip().split())
    e_x, e_y = map(int, sys.stdin.readline().rstrip().split())

    print(bfs(x, y, e_x, e_y, N))