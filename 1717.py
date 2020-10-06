import sys

n, m = map(int, sys.stdin.readline().split())
infos = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
root = [i for i in range(n+1)]

def find(x) :
    if root[x] == x:
        return x
    else :
        root[x] = find(root[x])
        return root[x]

for info in infos :
    if info[0] == 0:
        root[find(info[2])] = find(info[1])
        print(info[1], info[2], root)
    else :
        if find(info[1]) == find(info[2]) :
            sys.stdout.write("YES\n")
        else :
            sys.stdout.write("NO\n")
print(root)