import sys
n, k = map(int, input().split() )

def bfs(x) :
    visited = [False] *100001
    queue =[x]
    state = False
    cnt = 0

    while (queue) :
        for _ in range(len(queue)) :
            current_x = queue.pop(0)
            if (visited[current_x] == False) :
                visited[current_x] = True
                if(current_x == k) :
                    state = True
                    break
                if  current_x-1>= 0 :
                    queue.append(current_x-1)
                if current_x+1 <= 100000:
                    queue.append(current_x+1)
                if 2*current_x <=100000 :
                    queue.append(2*current_x)
        if state :
            print(cnt)
            break
        cnt +=1
bfs(n)
