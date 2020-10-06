def dp(x, arr) :
    if x % 6 == 0:
        arr[x] = min(arr[x//2]+1, arr[x//3]+1, arr[x-1]+1)
    elif x % 3 == 0 :
        arr[x] = min(arr[x // 3] + 1, arr[x - 1] + 1)
    elif x % 2 == 0 :
        arr[x] = min(arr[x//2]+1, arr[x-1]+1)
    else :
        arr[x] = arr[x-1]+1
n = int(input())
if n ==1 :
    print(0)
elif n ==2 or n== 3 :
    print(1)
else :
    used_cnt = [0, 0, 1, 1]+ [0] *(n-3)
    for i in range(4, n+1) :
        dp(i, used_cnt)
    print(used_cnt[n])