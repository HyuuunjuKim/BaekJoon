a= int(input())

if a in range(1, 10001) :
    sum = 0
    for i in range(1, a+1) :
        sum = sum + i
    print(sum)