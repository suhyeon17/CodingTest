import sys
from collections import deque

def bfs(graph, virus, N, S):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque(virus)

    while q:
        num, time, x, y = q.popleft()
        if time == S:
            return
        for i in range(4):
           nx = x + dx[i]
           ny = y + dy[i]
           
           if 0<=nx<N and 0<=ny<N and graph[ny][nx]==0:
               graph[ny][nx] = num
               q.append((graph[ny][nx], time+1, nx, ny))
    
    return

N, K = map(int, sys.stdin.readline().rstrip().split())
graph = []
virus = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(N):
        if graph[i][j] != 0:
            virus.append((graph[i][j], 0, j, i))
S, X, Y = map(int, sys.stdin.readline().rstrip().split())

virus.sort()
bfs(graph, virus, N, S)
print(graph[X-1][Y-1])
