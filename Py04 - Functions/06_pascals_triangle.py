from math import factorial


def pascal(n):
    result = ''
    for l in range(n):
        for n in range(0, l+1):
            result += str(int(factorial(l) /
                          (factorial(n) * factorial(l-n)))) + ' '
        result = result.strip(' ')
        result += '\n'
    return result
