from itertools import combinations_with_replacement

n, m = map(int, input().split())

arr = [str(i) for i in range(1, n+1)]
nCr_2 = list(combinations_with_replacement(arr, m))

for i in nCr_2:
        print(" ".join(i))