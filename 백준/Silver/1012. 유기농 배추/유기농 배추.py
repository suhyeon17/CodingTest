import sys
from collections import deque

def bfs(graph, x, y, N, M, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((x, y))
    visited[y][x] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<M and 0<=ny<N and graph[ny][nx] == 1 and visited[ny][nx] != True:
                q.append((nx, ny))
                visited[ny][nx] = True
                

T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    graph = [[0] * M for _ in range(N)]
    for _ in range(K):
        c, r = map(int, sys.stdin.readline().rstrip().split())
        graph[r][c] = 1
    
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    for r in range(N):
        for c in range(M):
            if graph[r][c] == 1 and visited[r][c] != True:
                bfs(graph, c, r, N, M, visited)
                cnt += 1

    print(cnt)