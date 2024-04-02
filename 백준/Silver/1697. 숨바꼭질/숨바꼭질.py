from collections import deque

def bfs(N, K, visited):
    dx = [-1, 1, 2]
    q = deque()
    q.append(N)

    while q:
        x = q.popleft()
        if x == K:
            return visited[K]
        for i in range(3):
            if i == 2:
                nx = x * dx[i]
            else:
                nx = x + dx[i]
            if 0<=nx<100001 and visited[nx] == 0:
                q.append(nx)
                visited[nx] = visited[x] + 1
    
N, K = map(int, input().split())

visited = [0] * 100001
print(bfs(N, K, visited))