a= int(input())

if a in range(1, 101) :
    for i in range(1, a+1) :
        print(" "*(i-1)+"*"*(a+1-i))