def rearrange(l):
    a = [x for x in l if x <= 0]
    b = [x for x in l if x > 0]
    return a + b
