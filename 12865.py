n, k = map(int, input().split())

info = [[0,0]]+[list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1) :
    for j in range(1, k+1) :
        if j < info[i][0] :
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-info[i][0]]+info[i][1]) #내꺼 안더할 때랑 내꺼 더 할때
print(dp[n][k])