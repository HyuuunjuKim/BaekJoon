def solution(exp) :
    res = 0
    list = [i for i in exp.replace('-', ' ').split()]
    for idx, val in enumerate(list):
        if idx == 0 :
            tmp = val.split("+")
            sum = 0
            for j in tmp :
                sum +=int(j)
            res += sum
        else :
            tmp = val.split("+")
            sum = 0
            for j in tmp:
                sum +=int(j)
            res -= sum
    return res

if __name__ == "__main__" :
    expression = input()
    print(solution(expression))

