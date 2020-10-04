n = int(input())
lopes = []
for _ in range(n):
    lopes.append(int(input()))
lopes.sort()
ans = 0
for i in range(n):
    possible_weight = (n-i) * lopes[i]
    if possible_weight > ans :
        ans = possible_weight
print(ans)