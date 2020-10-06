from collections import deque
from itertools import combinations
n, m = map(int, input().split())
area =[list(map(int, input().split())) for _ in range(n)]
zero_info= []
for i in range(n) :
    for j in range(m) :
        if area[i][j] == 0 :
            zero_info.append([i, j])
# function1 - 바이러스 퍼지기
def spread_virus(graph, visited, v) :
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    queue = deque([v])
    visited[v[0]][v[1]] = True
    while queue :
        cur = queue.popleft()
        for i in range(4) :
            nx = cur[0] + dx[i]
            ny = cur[1] + dy[i]
            if 0<= nx <n and 0 <=ny < m :
                if (not visited[nx][ny]) and graph[nx][ny] == 0 :
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                    graph[nx][ny] = 2

# function2 - 0의 개수 세기
def cnt_safezone(graph, cnt) :
    for i in range(n) :
        for j in range(m) :
            if graph[i][j] == 0 :
                cnt+=1
    return cnt

'''
1. 3개의 0을 1로 바꾼다
2. 바이러스를 퍼뜨린다
3. 0의 개수를 센다.
'''
nC3 = combinations(zero_info, 3)
ans = 0
for i in nC3 :
    graph = []
    count = 0
    for row in area :
        graph.append(row[:])
    for j in i :
        graph[j[0]][j[1]] = 1
    visit_status = [[False]*m for _ in range(n)]
    for row in range(n) :
        for col in range(m) :
            if (not visit_status[row][col]) and graph[row][col] == 2 :
                spread_virus(graph, visit_status, [row, col])
    zero_cnt = cnt_safezone(graph, count)
    if ans < zero_cnt  : ans = zero_cnt
print(ans)

