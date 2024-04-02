from collections import deque

def bfs(N, K, visited):
    dx = [-1, 1, 2]
    q = deque()
    q.append(N)
    cnt = 0

    while q:
        x = q.popleft()
        if x == K:
            cnt += 1
        for i in range(3):
            if i == 2:
                nx = x * dx[i]
            else:
                nx = x + dx[i]
            if 0<=nx<100001 and (visited[nx] == 0 or visited[nx] == visited[x] + 1):
                q.append(nx)
                visited[nx] = visited[x] + 1
    
    return visited[K], cnt

N, K = map(int, input().split())

visited = [0] * 100001
if N == K:
    time, way = 0, 1
else:
    time, way = bfs(N, K, visited)

print(time)
print(way)