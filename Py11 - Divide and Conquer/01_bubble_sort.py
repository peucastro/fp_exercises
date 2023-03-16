def bubble_sort(alist):
    flag = False
    while not flag:
        flag = True
        for n in range(len(alist)-1):
            if alist[n] > alist[n+1]:
                flag = False
                alist[n], alist[n+1] = alist[n+1], alist[n]
    return alist
