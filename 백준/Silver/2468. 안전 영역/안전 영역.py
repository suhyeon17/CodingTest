import sys
from collections import deque

def bfs(graph, visited, x, y, N, safe):
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

            if 0<=nx<N and 0<=ny<N and not visited[ny][nx] and graph[ny][nx] > safe:
                q.append((nx, ny))
                visited[ny][nx] = True
    return 1

N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split(' '))))

#가능한 안전 영역의 범위
m, n = 2, 100
for i in range(N):
    if max(graph[i])>=m:
        m = max(graph[i])
    if min(graph[i])<=n:
        n = min(graph[i])

#탐색
answer = []
for safe in range(n-1, m+1):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > safe and not visited[i][j]:
                cnt += bfs(graph, visited, j, i, N, safe) 

    answer.append(cnt)

print(max(answer))