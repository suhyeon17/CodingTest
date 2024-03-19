import sys
from collections import deque

def bfs(graph, x, y, N, M):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False] * M for _ in range(N)]
    cnt = [[0] * M for _ in range(N)]
    q = deque()
    q.append((x, y))
    visited[y][x] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<M and 0<=ny<N and not visited[ny][nx] and graph[ny][nx] == 1: 
                q.append((nx, ny))
                visited[ny][nx] = True
                cnt[ny][nx] = cnt[y][x] + 1
    return cnt[N-1][M-1] + 1


N, M = map(int, sys.stdin.readline().rstrip().split())
graph = []

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

print(bfs(graph, 0, 0, N, M))