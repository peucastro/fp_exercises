def bitonic_point(f):
    alist = f()
    middle = len(alist) // 2
    mininum = 0
    maximum = len(alist)

    while not (alist[middle - 1] < alist[middle] and alist[middle + 1] < alist[middle]):
        if alist[middle - 1] < alist[middle]:
            mininum = middle
        else:
            maximum = middle

        middle = mininum + (maximum - mininum) // 2

    return alist[middle]


print(bitonic_point(lambda: [2, 6, 10, 25, 60, 30, 25, 10, 0]))
