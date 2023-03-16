from functools import reduce

def map_filter_reduce(lst, f1, f2, f3):
    lista = list(filter(f1, lst))
    listb = list(map(f2, lista))

    return reduce(f3, listb)
