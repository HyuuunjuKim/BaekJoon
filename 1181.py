import sys
import re

arr = [word.replace('\n', '') for word in sys.stdin]
arr2 = arr[1:]
tmp = set(arr2)
arr3 = list(tmp)
arr3.sort(key = lambda x : [len(x), x])

for i in arr3 :
    print(i)