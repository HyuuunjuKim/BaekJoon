n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)
ans = 0
for item in coins :
    if item <= k :
        ans += k // item
        k = k - (k // item)*item
    else :
        continue

print(ans)