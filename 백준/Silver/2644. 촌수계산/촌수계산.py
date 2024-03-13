import sys
from collections import deque

def bfs(graph, start, end, visited, result):
    cnt = 0
    q = deque([start])
    visited[start] = True

    while q:
        n = q.popleft()
        if n == end:
            return result[end]          
        for i in graph[n]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                result[i] = result[n] + 1
    return -1

N = int(sys.stdin.readline())
p1, p2 = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for i in range(1, M+1):
    num1, num2 = map(int, sys.stdin.readline().split())
    graph[num1].append(num2)
    graph[num2].append(num1)
    graph[num1].sort()
    graph[num2].sort()

visited = [False] * (N+1)
result = [0] * (N+1)
print(bfs(graph, p1, p2, visited, result))