from collections import deque

def bfs(graph, visited, start):
    q = deque()
    q.append(start)
    visited[start] = True
    
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                
                
def solution(n, computers):
    answer = 0
    
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] and i != j:
                graph[i].append(j)
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            bfs(graph, visited, i)
            answer += 1
            
    return answer
            
        