import sys
from collections import deque

def bfs(graph, start, visited):
    q = deque()
    q.append(start)
    visited[start] = True
    cnt = 0

    while q:
        n = q.popleft()
        for v in graph[n]:
            if not visited[v]:
                q.append(v)
                visited[v] = True
                cnt += 1

    return cnt



N = int(sys.stdin.readline())
V = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]

for i in range(V):
    num1, num2 = map(int, sys.stdin.readline().rstrip().split())
    graph[num1].append(num2)
    graph[num2].append(num1)
    graph[num1].sort()
    graph[num2].sort()

visited = [False] * (N+1)
print(bfs(graph, 1, visited))