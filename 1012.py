from collections import deque

case_count = int(input())
for _ in range(case_count) :
    cnt = 0
    def bfs(start) :
        global cnt

        # L, R, U, D 순
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        queue = deque([start])
        while queue :
            current  = queue.popleft()
            for i in range(4):
                ny = current[0] + dy[i]
                nx = current[1] + dx[i]
                if 0<=nx <m and 0 <=ny < n :
                    if visited[ny][nx] == False and ground[ny][nx] == 1 :
                        visited[ny][nx] = True
                        queue.append([ny, nx])

        cnt +=1

    m, n, k = map(int, input().split())
    ground = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    infos = []
    for _ in range(k) :
        x, y = map(int, input().split())
        infos.append([y, x])
        ground[y][x] = 1
    for info in infos:
        if not visited[info[0]][info[1]] :
            bfs(info)

    print(cnt)