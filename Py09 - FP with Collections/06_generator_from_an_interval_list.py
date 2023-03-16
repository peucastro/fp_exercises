def generator(intlist):
    for tup in intlist:
        for a in range(tup[0], tup[1]+1):
            yield a
