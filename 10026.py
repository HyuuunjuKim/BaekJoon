import sys
sys.setrecursionlimit(10000)

n = int(input())
picture = []
picture2 = []
visited = []
visited2 = []
for _ in range(n):
    tmp =list(sys.stdin.readline())
    picture.append(tmp)
    visited.append([False]*n)
    visited2.append([False] * n)
    tmp3 = []
    for i in tmp :
        tmp2 = i.replace("R", "G")
        tmp3.append(tmp2)
    picture2.append(tmp3)

def dfs(graph, v, visited) :
    # L, R, D, U 순
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    # v가 좌표 형태
    visited[v[0]][v[1]] = True
    for i in range(4):
        nx = v[0] + dx[i]
        ny = v[1] + dy[i]
        if 0 <= nx < n and 0 <= ny < n :
            if (not visited[nx][ny]) and graph[v[0]][v[1]] == graph[nx][ny] :
                dfs(graph, [nx, ny], visited)
ans1 = 0
for i in range(n) :
    for j in range(n) :
        if not visited[i][j] :
            dfs(picture, [i, j], visited)
            ans1 +=1
print(ans1, end=' ')

ans2 = 0
for i in range(n) :
    for j in range(n) :
        if not visited2[i][j] :
            dfs(picture2, [i, j], visited2)
            ans2 +=1
print(ans2)
