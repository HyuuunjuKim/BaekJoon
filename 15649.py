from itertools import permutations

n, m = map(int, input().split())

arr = [str(i) for i in range(1, n+1)]
nPr = list(permutations(arr, m))
for i in nPr :
    print(' '.join(i))

