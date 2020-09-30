from itertools import permutations

n = int(input())
arr = [i for i in input().split()]

operator = []
for idx, count in enumerate(input().split()):
    if idx == 0 :
        for _ in range(int(count)) : operator.append('+')
    elif idx == 1 :
        for _ in range(int(count)) : operator.append('-')
    elif idx == 2 :
        for _ in range(int(count)) : operator.append('*')
    else:
        for _ in range(int(count)) : operator.append('//')
ans = []
for i in set(permutations(operator, len(operator))):
    tmp  = arr[:]
    for idx, j in enumerate(i) :
        if idx == 0 :
            if len(i) != 1:
                tmp.insert(1, j)
            else :
                tmp.insert(1, j)

                last_res = 0
                if int(tmp[0]) < 0 and int(tmp[2]) > 0 and tmp[1] == "//":
                    last_res = -1 * (-1 * int(tmp[0]) // int(tmp[2]))
                else:
                    last_res = eval("".join(tmp[0:3]))

                if (len(ans) < 2):
                    ans.append(int(last_res))
                    ans.sort()
                else:
                    if int(last_res) < ans[0]:
                        del ans[0]
                        ans.insert(0, int(last_res))
                    elif int(last_res) > ans[1]:
                        del ans[1]
                        ans.append(int(last_res))
                    else:
                        continue
        elif idx == len(i) -1 :
            if int(tmp[0]) < 0 and int(tmp[2]) >0 and tmp[1] == "//" :
                res = str(-1*(-1*int(tmp[0]) //int(tmp[2])))
            else :
                res = eval("".join(tmp[0:3]))
            del tmp[:3]
            tmp.insert(0, str(res))
            tmp.insert(1, j)

            last_res = 0
            if int(tmp[0]) < 0 and int(tmp[2]) > 0 and tmp[1] == "//":
                last_res = -1 * (-1 * int(tmp[0]) // int(tmp[2]))
            else:
                last_res = eval("".join(tmp[0:3]))

            if(len(ans) < 2):
                ans.append(int(last_res))
                ans.sort()
            else:
                if int(last_res) < ans[0] :
                    del ans[0]
                    ans.insert(0, int(last_res))
                elif int(last_res) > ans[1]:
                    del ans[1]
                    ans.append(int(last_res))
                else :
                    continue
        else :
            if int(tmp[0]) < 0 and int(tmp[2]) >0 and tmp[1] == "//" :
                res = str(-1*(-1*int(tmp[0]) //int(tmp[2])))
            else:
                res = eval("".join(tmp[0:3]))
            del tmp[:3]
            tmp.insert(0, str(res))
            tmp.insert(1, j)
if len(ans) ==1 :
    print(ans[0])
    print(ans[0])
else :
    print(ans[1])
    print(ans[0])