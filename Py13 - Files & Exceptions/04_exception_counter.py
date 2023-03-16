def count_exceptions(f, n1, n2):
    count = 0
    for n in range(n1, n2+1):
        try:
            f(n)
        except:
            count += 1
    return count
