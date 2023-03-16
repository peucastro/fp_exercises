def count_until(tup):
    count = 0
    for e in tup:
        if type(e) != tuple:
            count += 1
        else:
            return count
    return -1
