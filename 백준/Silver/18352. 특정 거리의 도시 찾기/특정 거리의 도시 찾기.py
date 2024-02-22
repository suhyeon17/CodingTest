import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    city1, city2 = map(int, input().split())
    graph[city1].append(city2)
##########################################

def bfs(graph, start, visited, cnt):
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                cnt[i] = cnt[v] + 1

    return cnt

answer = []
cnt = [0] * (N+1)
visited = [False] * (N+1)
cnt = bfs(graph, X, visited, cnt)

for idx, c in enumerate(cnt):
    if c == K:
        answer.append(idx)

if answer:
    for a in answer:
        print(a)
else: print(-1)