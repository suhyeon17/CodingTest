from collections import deque

def bfs(graph, start, visited):
    cnt = 0
    q = deque([start])
    visited[start] = True
    
    while q:
        cnt += 1
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
    return cnt
        
def solution(n, wires):
    answer = []
    
    for i in range(len(wires)):
        tmp = wires.copy()
        graph = [[] for _ in range(n+1)]
        visited = [False] * (n+1)
        
        tmp.pop(i)
        for t in tmp:
            x, y = t
            graph[x].append(y)
            graph[y].append(x)
            
        for idx, g in enumerate(graph):
            if g:
                start = idx
                break
        conn = bfs(graph, start, visited)
        other = n - conn
        answer.append(abs(conn-other))
        
    return min(answer)