x, y =input().split()
real_days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekdays= ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

if int(x) in range(1, 13) :
    sum=0
    for i in range(1, int(x)) :
        sum= sum + real_days[i-1]
    if int(y) in range(1, 32) :
        sum_days= sum + int(y)
    num_weekday= sum_days % 7
    print(weekdays[num_weekday-1])
    