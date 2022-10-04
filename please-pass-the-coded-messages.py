from itertools import combinations
def solution(l):
# digit matters! The more digit, the bigger
# choose 9? return: choose 8
# Towards choose 1
    n = len(l)
    res = 0;
    # iterate n times
    for i in range(n):
        # create list of list,
        # containing all possible combinations
        tmp = combinations(l,i+1)
        for row in tmp:
            if listCheck(row):
               res = max(res,constructNumber(row))
    return res

def listCheck(x):
    # a number can be divided by three if and only if
    # all the digits can add up to three
    sum = 0
    for i in x:
        sum += i

    if sum % 3 == 0:
        return True
    else:
        return False

def constructNumber(l):
    # construct a number from the list
    l = list(l)
    l.sort(reverse=True)
    n = len(l)
    res = 0
    for i in l:
        n -= 1
        res += i*(10**n)
    return res

x = [3,4,1,1]
print(solution(x))
