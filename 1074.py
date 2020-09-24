path = []

def divide(n, r, c) :
    global path
    if  n ==1 :
        if r==1 and c==1 :
            path.append(3)
            return path
        elif r == 0 and c==0:
            path.append(0)
            return path
        elif r ==1 and c ==0 :
            path.append(2)
            return path
        elif r == 0 and c ==1 :
            path.append(1)
            return path

    if(2**n) // 2 <= r and (2**n) // 2 <= c :
        r -= (2**n) // 2
        c -= (2 ** n) // 2
        path.append(3)
    elif(2**n) // 2 <= r and (2**n) //2 > c :
        r -= (2**n) //2
        path.append(2)
    elif (2 ** n) // 2 > r and (2 ** n) // 2 <= c:
        c -= (2 ** n) // 2
        print(r, c)
        path.append(1)
    elif (2**n) // 2 > r and (2**n) // 2 > c:
        path.append(0)

    n -=1
    return divide(n, r, c)

N, y, x = map(int, input().split())
divide(N,y,x)

ans = 0
path.reverse()
for idx, item in enumerate(path) :
    ans +=(4**idx)*item
print(ans)