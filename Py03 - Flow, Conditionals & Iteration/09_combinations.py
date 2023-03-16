def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n-1)


def C(n, r):
    if n == r:
        return 1
    return int(fact(n)) / (fact(r)*fact(n-r))
