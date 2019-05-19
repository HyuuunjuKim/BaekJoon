a= int(input())

if (a >=1) and (a <=100) :
    for i in range(1, a+1) :
        print(" "*(a-i) + "*"*i)