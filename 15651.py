from itertools import product

n, m = map(int, input().split())

arr = [str(i) for i in range(1, n+1)]
nPr_2 = list(product(arr, repeat = m))

for i in nPr_2:
    print(" ".join(i))