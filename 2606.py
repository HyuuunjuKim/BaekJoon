from collections import Counter

n = int(input())
m = int(input())
networks = [[]for _ in range(n+1)]
for _ in range(m):
    start, end = map(int, input().split())
    networks[start].append(end)
    networks[end].append(start)
visit_status = [False]*(n+1)

def dfs(graph, v, visited) :
    visited[v] = True
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)

dfs(networks, 1, visit_status)
print(Counter(visit_status)[True] -1)