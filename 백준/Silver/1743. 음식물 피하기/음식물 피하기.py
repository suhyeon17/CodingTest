import sys
from collections import deque

def bfs(graph, visited, x, y, N, M):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((x, y))
    visited[y][x] = True
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<M and 0<=ny<N and graph[ny][nx] == 1 and not visited[ny][nx]:
                q.append((nx, ny))
                visited[ny][nx] = True
                cnt += 1

    return cnt

N, M, K = map(int, sys.stdin.readline().rstrip().split())
graph = [[0]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]
for i in range(K):
    r, c = map(int, sys.stdin.readline().rstrip().split())
    graph[r-1][c-1] = 1

answer = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visited[i][j]:
           answer.append(bfs(graph, visited, j, i, N, M))

print(max(answer))

        
        
