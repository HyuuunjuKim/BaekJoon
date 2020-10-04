import sys

n = int(input())
triangle = []
for _ in range(n):
    triangle.append([int(x) for x in sys.stdin.readline().split()])

for col in range(n-2, 0, -1) :
    for idx in range(col+1) :
        triangle[col][idx] += max(triangle[col+1][idx],triangle[col+1][idx+1])

ans = triangle[0][0] + max(triangle[1][0], triangle[1][1])
print(ans)