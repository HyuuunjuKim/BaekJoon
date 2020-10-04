n = int(input())
p = [int(x) for x in input().split()]
p.sort()
sum =0
for i in range(n) :
    sum += (n-i)*p[i]
print(sum)