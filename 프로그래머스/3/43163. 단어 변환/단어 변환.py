from collections import deque

def diff(word1, word2):
    cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cnt += 1
        
        if cnt >= 2:
            return False
        
    if cnt == 1:
        return True

def bfs(begin, target, graph):
    visited = {}
    for k in graph:
        visited[k] = False


    q = deque()
    q.append((begin, 0))
    visited[begin] = True

    
    while q:
        n, cnt = q.popleft()
        if n == target:
            return cnt
        for v in graph[n]:
            if not visited[v]:
                q.append((v, cnt + 1))
                visited[v] = True
        
def solution(begin, target, words):
    if target not in words:
        return 0
    graph = {}
    graph[begin] = []
    for w in words:
        graph[w] = []
        
    for i, k in enumerate(graph):
        for j in range(i, len(words)):
            if diff(k, words[j]):
                graph[k].append(words[j])
                graph[words[j]].append(k)
    
    answer = bfs(begin, target, graph)
    return answer
                