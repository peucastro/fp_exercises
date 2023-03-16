def aux(alist, step, index):
    if len(alist) > 1:
        index = (index + step-1) % len(alist)
        alist.pop(index)
        return aux(alist, step, index)
    elif len(alist) == 1:
        return alist[0]


def last_man_standing(alist, step):
    index = 0
    if len(alist) > 1:
        index = (index + step-1) % len(alist)
        alist.pop(index)
    return aux(alist, step, index)
