import sys
sys.setrecursionlimit(10000)

n, m  = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m) :
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)
visited = [False] * (n+1)
cnt = 0
def dfs(graph, v, visited) :
    visited[v] = True
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)

for i in range(1, n+1) :
    if not visited[i]:
        dfs(graph, i, visited)
        cnt += 1
print(cnt)