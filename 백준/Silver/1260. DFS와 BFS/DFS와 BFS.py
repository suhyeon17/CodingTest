import sys
from collections import deque

def bfs(graph, start, visited):
    visited[start] = True
    q = deque([start])
    
    while q:
        v = q.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end = ' ')

    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


N, M, V = map(int, sys.stdin.readline().split()) 
graph = [[] for _ in range(N+1)]
for _ in range(M):
    node1, node2 = map(int, sys.stdin.readline().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
    graph[node1].sort()
    graph[node2].sort()

visit1 = [False] * (N+1)
visit2 = [False] * (N+1)

dfs(graph, V, visit1)
print()
bfs(graph, V, visit2)
