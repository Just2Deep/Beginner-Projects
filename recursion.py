# Recursion

num = 5


def SumNum(num):
    if num == 1:
        return 1
    return num + SumNum(num-1)


print(SumNum(num))
