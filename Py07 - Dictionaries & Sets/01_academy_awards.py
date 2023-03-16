def academy_awards(alist):   
    blist = []
    clist = []
    counter = []
    res = {}
    for cat, fil in alist:
        blist.append(fil)
    for i in blist:
        if i in clist:
            continue
        else:
            clist.append(i)
    for i in clist:
        counter.append(blist.count(i))
    prevres = zip(clist, counter)
    for i, j in prevres:
        res[i] = j
    return res
