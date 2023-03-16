def reciprocals(alist):
    res = []
    for n in alist:
        try:
            res.append(1/n)
        except:
            pass
    return res
